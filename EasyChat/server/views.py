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
        # Get the category id from the request
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == 'true'
        by_serverid = request.query_params.get("by_serverid")

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

        if qty:
            self.queryset = self.queryset[: int(qty)]

        if by_serverid:
            try:
                self.queryset = self.queryset.filter(id=by_serverid) # Django will automatically create id
                if not self.queryset.exists():
                    raise ValidationError(detail=f"Server with id {by_serverid} not found")
            except ValueError:
                raise ValidationError(detail="Server value error")


        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)

