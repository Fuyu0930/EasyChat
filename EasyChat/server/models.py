from django.conf import settings
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Server(models.Model):
    name = models.CharField(max_length=100)

    # Build a relationship to the User table
    # If the owner were deleted from the system, then the server will also be deleted
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="server_owner")

    # One server is connected to one category (one to one)
    # One category could be connected to many servers (one to many)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="server_category")

    description = models.CharField(max_length=250, blank = True, null=True)

    # One server could have multiple members
    # One member could have multiple servers
    # Many to many relationship
    member = models.ManyToManyField(settings.AUTH_USER_MODEL)
    
    def __str__(self):
        return self.name

# One server has multiple channels
# One channel only has one server
class Channel(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="channel_owner")
    topic = models.CharField(max_length=100)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="channel_server")

    # When we save anything from the table, we are going to extra tasks
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Channel, self).save(*args, **kwargs)


    def __str__(self):
        return self.name