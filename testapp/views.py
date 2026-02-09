from django.shortcuts import render, redirect
from .models import YourGoals, UniversalChat
from .forms import SendChat


# Create your views here.
def home(request):
    return render(request, "home.html")


def goals(request):
    goals_list = YourGoals.objects.all()
    return render(request, "goals.html", {'goals': goals_list})


def chats(request):
    allchats = UniversalChat.objects.all()
    if request.POST:
        form = SendChat(request.POST, request.POST)
        if form.is_valid():
            user_chat = form.save(commit=False)
            user_chat.text_id = "hehe123"
            user_chat.save()
            print(f"IP hehe: {request.META.get('REMOTE_ADDR')}")
            return redirect(chats)
        return redirect(home)

    return render(request,
                  "testchat.html",
                  {'all_chats': allchats, 'form': SendChat})
