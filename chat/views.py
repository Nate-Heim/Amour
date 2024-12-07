from django.shortcuts import render

def chatPage(request, room_name):
    return render(request, 'chat/chatPage.html', {
        'room_name': room_name,
        'username': request.user.username,
    })