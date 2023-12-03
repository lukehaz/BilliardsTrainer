from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CreateNewUser, loginForm, MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .models import User, Stats, Message
from .models import Drill_data

# Create your views here.
def welcome(request):
    return render(request, 'main_app/welcome.html')

#DB
@login_required(login_url='/login/')
def profile(response, id):
    prof = User.objects.get(id=id)
    return render(response, "main_app/profile.html", {"prof":prof})

def create(request):
    if (request.method == "POST"):
        form = CreateNewUser(request.POST)

        if form.is_valid():
            New_User = form.save()
            New_User.set_password(New_User.password)
            New_User.save()
            
            return redirect("/login")
    else:
        form = CreateNewUser()
    return render(request, "main_app/create.html",{"form":form})

#login
def user_login(request):
    if request.method == "POST":
        login_form = loginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return redirect("/") #redirect to desired page
                else:#account is inactive
                    return HttpResponse("Account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, "main_app/login.html", {"login_form":loginForm})
    else:
        return render(request, "main_app/login.html",{"login_form":loginForm})

#logout
def user_logout(request):
        logout(request)
        return redirect("/")

@login_required(login_url='/login/')
def message_list(request):
    # Query the database for messages and pass them to the template
    messages = Message.objects.all()
    context = {'messages': messages}
    return render(request, 'main_app/message_list.html', context)

@login_required(login_url='/login/')
def add_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message to the database
            return redirect('message_list')  # Redirect to the message list page

    else:
        form = MessageForm()

    context = {'form': form}
    return render(request, 'main_app/message_form.html', context)



#Drills

def drills(request):
    return render(request,'main_app/Drills/drills.html')

def Fundamentals(request):
    return render(request,'main_app/Drills/fundamentals.html')

def Shotmaking(request):
    return render(request,'main_app/Drills/Shotmaking.html')

def Kicking(request):
    return render(request,'main_app/Drills/kicking.html')

def Banking(request):
    return render(request,'main_app/Drills/banking.html')

def Safety(request):
    return render(request,'main_app/Drills/Safety.html')

def Jumping(request):
    return render(request,'main_app/Drills/Jumping.html')
#fundamentals
def stop(request):
    return render(request,'main_app/Drills/fundamentals/stop.html')

def follow(request):
    return render(request,'main_app/Drills/fundamentals/follow.html')

def draw(request):
    return render(request,'main_app/Drills/fundamentals/draw.html')


#shotmaking
def mill(request):
    if request.method == "POST":
        username = request.POST["username"]
        drill_name = request.POST["drill_name"]
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=username,drill_name=drill_name,amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/shotmaking/mill.html')

def everest(request):
    if request.method == "POST":
        username = request.POST["username"]
        drill_name = request.POST["drill_name"]
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=username,drill_name=drill_name,amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/shotmaking/everest.html')

def ladder(request):
    if request.method == "POST":
        username = request.POST["username"]
        drill_name = request.POST["drill_name"]
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=username,drill_name=drill_name,amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/shotmaking/ladder.html')

def corner(request):
    if request.method == "POST":
        username = request.POST["username"]
        drill_name = request.POST["drill_name"]
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=username,drill_name=drill_name,amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/shotmaking/corner.html') 

def train (request):
    if request.method == "POST":
        username = request.POST["username"]
        drill_name = request.POST["drill_name"]
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=username,drill_name=drill_name,amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/shotmaking/train.html')
           
def follower(request):
    if request.method == "POST":
        username = request.POST["username"]
        drill_name = request.POST["drill_name"]
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=username,drill_name=drill_name,amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/shotmaking/follower.html')   

