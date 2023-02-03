from .models import Room, Message
from django import forms


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('user', 'content')


class RoomCreateForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ['name', 'slug', 'author']
