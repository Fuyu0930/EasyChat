from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Server
from .serializer import ServerSerializer


# Start to build our endpoints
class ServerListViewSet(viewsets.ViewSet):

    queryset = Server.objects.all()

    def list(self, request):
        # Get the category id from the request
        category = request.query_params.get("category")
    
        if category:
            # Filter all the servers from the category id
            self.queryset = self.queryset.filter(category__name=category) # allows us to access the category name

        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)

