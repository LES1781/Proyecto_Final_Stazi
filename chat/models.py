from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Room(models.Model):

    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='rooms', null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.name


class Message(models.Model):

    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('date_added',)
    
    def __str__(self):
        return 'message {} by {}'.format(self.content, self.user)
