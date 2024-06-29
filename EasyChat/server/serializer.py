from rest_framework import serializers

from .models import Category, Channel, Server


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"

class ServerSerializer(serializers.ModelSerializer):
    # The code will also grab all channels related to the server
    # We have a foriegn key in the model 
    channel_server = ChannelSerializer(many=True) 

    class Meta:
        model = Server
        # Define the data we are going to return
        fields = "__all__"
        