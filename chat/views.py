from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Room
from .forms import MessageForm


class RoomList(generic.ListView):

    queryset = Room.objects.filter(status=1).order_by('-created_on')
    template_name = 'room_list'


class RoomCreate(LoginRequiredMixin, generic.CreateView):

    model = Room
    fields = ['name', 'slug']
    success_url = reverse_lazy('room_list')
    template_name = "chat/room_create.html"


def room_detail(request, slug):

    room = get_object_or_404(Room, slug=slug)
    messages = room.messages.filter(active=True)
    new_message = None

    if request.method == 'POST':

        message_form = MessageForm(data=request.POST)

        if message_form.is_valid():
            new_message = message_form.save(commit=False)
            new_message.room = room
            new_message.save()

    else:
        message_form = MessageForm()

    return render(
        request, 
        template_name='chat/room_detail.html',
        context={'room': room,
        'messages': messages,
        'new_message': new_message,
        'message_form': message_form}
        )
