from django.db.models import Count
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Server
from .schema import server_list_docs
from .serializer import ServerSerializer


# Start to build our endpoints
class ServerListViewSet(viewsets.ViewSet):

    queryset = Server.objects.all()
    permission_classes = [IsAuthenticated];

    @server_list_docs
    def list(self, request):
        """
        List servers based on various query parameters.

        This method filters and returns a list of servers based on the 
        specified query parameters. The parameters can filter by category,
        user, server ID, and whether to include the number of members.

        `Args`:
            request (HttpRequest): The HTTP request object containing query 
                parameters and user information.

        `Query Parameters`:
        
            - `category (str, optional)`: The category name to filter servers by. 
                If provided, only servers belonging to this category will be returned.

            - `qty (int, optional)`: The maximum number of servers to return. If provided,
                limits the number of returned servers to this quantity.

            - `by_user (bool, optional)`: If set to 'true', filters servers by the logged-in user.
                Requires the user to be authenticated.

            - `by_serverid (str, optional)`: The server ID to filter by. If provided, 
                only the server with this ID will be returned. Requires the user to be authenticated.

            - `with_num_memebers (bool, optional)`: If set to 'true', includes the number of members 
                in the server data.

        `Raises`:
            AuthenticationFailed: If the user is not authenticated and attempts
                to filter by user or server ID.
            ValidationError: If the server ID is not found or is invalid.

        `Returns`:
            Response: A Django REST framework Response object containing the 
                serialized server data, which is a list of servers matching the query parameters.
                If `with_num_memebers` is true, each server object includes the number of members.
        """
        # Get the category id from the request
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == 'true'
        by_serverid = request.query_params.get("by_serverid")
        with_num_memebers = request.query_params.get("with_num_memebers") == 'true'
    
        if category:
            # Filter all the servers from the category id
            self.queryset = self.queryset.filter(category__name=category) # allows us to access the category name

        if by_user:
            if by_user and request.user.is_authenticated:
                user_id = request.user.id
                self.queryset = self.queryset.filter(member=user_id)
            else:
                raise AuthenticationFailed()
        
        if with_num_memebers:
            self.queryset = self.queryset.annotate(num_members=Count("member"))

        if by_serverid:
            if not request.user.is_authenticated:
                raise AuthenticationFailed()
            
            try:
                self.queryset = self.queryset.filter(id=by_serverid) # Django will automatically create id
                if not self.queryset.exists():
                    raise ValidationError(detail=f"Server with id {by_serverid} not found")
            except ValueError:
                raise ValidationError(detail="Server value error")
        
        if qty:
            self.queryset = self.queryset[: int(qty)]


        serializer = ServerSerializer(self.queryset, many=True, context={"num_members": with_num_memebers})
        return Response(serializer.data)

