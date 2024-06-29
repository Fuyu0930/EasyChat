from rest_framework import serializers

from .models import Category, Server


class ServerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        # Define the data we are going to return
        fields = "__all__"
        