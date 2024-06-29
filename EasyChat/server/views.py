from django.db.models import Count
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response

from .models import Server
from .serializer import ServerSerializer


# Start to build our endpoints
class ServerListViewSet(viewsets.ViewSet):

    queryset = Server.objects.all()

    def list(self, request):
        """List servers based on various query parameters.

        This method filters and returns a list of servers based on the 
        specified query parameters. The parameters can filter by category,
        user, server ID, and whether to include the number of members.

        Args:
            request (HttpRequest): The HTTP request object containing query 
                parameters and user information.

        Query Parameters:
            category (str): The category name to filter servers by.
            qty (int): The quantity of servers to return.
            by_user (bool): Whether to filter servers by the logged-in user.
            by_serverid (str): The server ID to filter by.
            with_num_memebers (bool): Whether to include the number of members 
                in the response.

        Raises:
            AuthenticationFailed: If the user is not authenticated and attempts
                to filter by user or server ID.
            ValidationError: If the server ID is not found or is invalid.

        Returns:
            Response: A Django REST framework Response object containing the 
                serialized server data.
        """
        # Get the category id from the request
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == 'true'
        by_serverid = request.query_params.get("by_serverid")
        with_num_memebers = request.query_params.get("with_num_memebers") == 'true'

        # If user is not login and they do want to check user and server, 
        # then raise authentication failed
        if by_user or by_serverid and not request.user.is_authenticated:
            raise AuthenticationFailed()
    
        if category:
            # Filter all the servers from the category id
            self.queryset = self.queryset.filter(category__name=category) # allows us to access the category name

        if by_user:
            user_id = request.user.id
            self.queryset = self.queryset.filter(member=user_id)
        
        if with_num_memebers:
            self.queryset = self.queryset.annotate(num_members=Count("member"))

        if qty:
            self.queryset = self.queryset[: int(qty)]

        if by_serverid:
            try:
                self.queryset = self.queryset.filter(id=by_serverid) # Django will automatically create id
                if not self.queryset.exists():
                    raise ValidationError(detail=f"Server with id {by_serverid} not found")
            except ValueError:
                raise ValidationError(detail="Server value error")


        serializer = ServerSerializer(self.queryset, many=True, context={"num_members": with_num_memebers})
        return Response(serializer.data)

