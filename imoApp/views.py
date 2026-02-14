from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import ImoItem
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import createImoForm


# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect(loginPage)

    allImo = ImoItem.objects.all().order_by('-id')
    pagin = Paginator(allImo, 6)
    where = request.GET.get('where_at')
    imos = pagin.get_page(where)

    return render(request, "home.html", {'Imos': allImo, 'perImo': imos})


# Creation tab
def createImoPage(request):
    if not request.user.is_authenticated:
        return redirect(loginPage)

    if request.method == "POST" and request.user.is_authenticated:
        name = request.user.get_username()
        opinion = request.POST.get('opinion')

        cleared_name = name[:21]
        cleared_opinion = opinion[:980]
        print(f"Username: {cleared_name} | Opinion: {cleared_opinion}")
        cond1 = (cleared_name.strip() != "")
        cond2 = (cleared_opinion.strip() != "")

        if cond1 and cond2:
            imo_record = ImoItem(user_name=cleared_name, user_opinion=cleared_opinion)
            imo_record.save()
            return redirect(home)
        else:
            messages.error(request, "All blank inputs. Please try again!")
            print("Fuk dude, this all blank.")
        return redirect(createImoPage)

    return render(request, "create-page.html")


# Register page
def registerPage(request):
    if request.user.is_authenticated:
        return redirect(home)

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect(registerPage)
    else:
        form = UserCreationForm()

    return render(request, "register-page.html", {'register_form': form})


# Login page
def loginPage(request):
    if request.user.is_authenticated:
        return redirect(home)

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(home)
        else:
            messages.error(request, "Password or Username is wrong.")
            return redirect(loginPage)
    else:
        form = AuthenticationForm()

    return render(request, "login-page.html", {'login_form': form})


# Logout link
def logoutPage(request):
    if request.method == "POST":
        logout(request)
        return redirect(home)

    return redirect(home)


# Delete a opinion
def deleteOpinion(request, opinion_id):
    if not request.user.is_authenticated:
        redirect(loginPage)
    elif request.method == "POST" and request.user.is_authenticated:
        imo_item = ImoItem.objects.get(pk=opinion_id)
        current_username = request.user.get_username()

        if imo_item.user_name == current_username:
            print("Deleting: ", imo_item.id)
            print("From: ", imo_item.user_name)
            imo_item.delete()
        else:
            print("Not allowed to delete this.")
        redirect(userPersonal)

    return redirect(home)


# User personal history
def userPersonal(request):
    if not request.user.is_authenticated:
        return redirect(loginPage)

    # Deleting an imo
    if request.method == "POST" and request.user.is_authenticated:
        deleteOpinion(request, request.POST.get('opinion-id'))
        return redirect(userPersonal)

    user_name = request.user.get_username()
    allImo = ImoItem.objects.all()
    imosFromUser = [i for i in allImo if i.user_name == user_name]

    return render(request, "personal.html", {'Imos': imosFromUser})
