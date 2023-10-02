from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
    return render(request, 'main_app/welcome.html')
  
  
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
    return render(request,'main_app/Drills/shotmaking/mill.html')

def everest(request):
    return render(request,'main_app/Drills/shotmaking/everest.html')

def ladder(request):
    return render(request,'main_app/Drills/shotmaking/ladder.html')

def corner(request):
    return render(request,'main_app/Drills/shotmaking/corner.html') 

def train (request):
    return render(request,'main_app/Drills/shotmaking/train.html')
           
def follower(request):
    return render(request,'main_app/Drills/shotmaking/follower.html')   

