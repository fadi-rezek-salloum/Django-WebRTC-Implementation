from django.shortcuts import render

def index(request):

    return render(request, 'chat/index.html', {})


def room(request):

    return render(request, 'chat/room.html', {})