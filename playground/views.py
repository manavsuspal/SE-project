from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from playground.models import *
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from playground.forms import RegistrationForm
from django.conf import settings
from django.db.models import Q
from .models import Event
from .forms import EventSearchForm
from django.contrib.auth import get_user_model
# from .forms import SearchForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
# from .forms import AlertForm
from django.contrib import messages
User = get_user_model()

stateCodes = {'Andhra Pradesh': 'AP', 'Arunachal Pradesh': 'AR', 'Assam': 'AS', 'Bihar': 'BR', 'Chhattisgarh': 'CG', 'Goa': 'GA', 'Gujarat': 'GJ', 'Haryana': 'HR', 'Himachal Pradesh': 'HP', 'Jammu and Kashmir': 'JK', 'Jharkhand': 'JH', 'Karnataka': 'KA', 'Kerala': 'KL', 'Madhya Pradesh': 'MP', 'Maharashtra': 'MH', 'Manipur': 'MN', 'Meghalaya': 'ML', 'Mizoram': 'MZ', 'Nagaland': 'NL', 'Odisha': 'OD', 'Punjab': 'PB', 'Rajasthan': 'RJ', 'Sikkim': 'SK', 'Tamil Nadu': 'TN', 'Telangana': 'TS', 'Tripura': 'TR', 'Uttarakhand': 'UK', 'Uttar Pradesh': 'UP', 'West Bengal': 'WB', 'Delhi': 'DL'}
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

@csrf_exempt
def home(request):
    context = {'states': stateCodes,'months':months}
    return render(request, 'home_page.html',context)

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                # return HttpResponse("Successful")
                # redirect_url = reverse('home')
                messages.success(request,("Login Successfull!"))

                return redirect('/playground/home/')
        else:
            return redirect('login')  
    else:
         return render(request,'login.html',{})

def userlogout(request):
    logout(request)
    messages.success(request,"You were logged out")
    return redirect('/playground/home/')
        

stateList={'AP': 'Andhra Pradesh', 'AR': 'Arunachal Pradesh', 'AS': 'Assam', 'BR': 'Bihar', 'CG': 'Chhattisgarh', 'GA': 'Goa', 'GJ': 'Gujarat', 'HR': 'Haryana', 'HP': 'Himachal Pradesh', 'JK': 'Jammu and Kashmir', 'JH': 'Jharkhand', 'KA': 'Karnataka', 'KL': 'Kerala', 'MP': 'Madhya Pradesh', 'MH': 'Maharashtra', 'MN': 'Manipur', 'ML': 'Meghalaya', 'MZ': 'Mizoram', 'NL': 'Nagaland', 'OD': 'Odisha', 'PB': 'Punjab', 'RJ': 'Rajasthan', 'SK': 'Sikkim', 'TN': 'Tamil Nadu', 'TS': 'Telangana', 'TR': 'Tripura', 'UK': 'Uttarakhand', 'UP': 'Uttar Pradesh', 'WB': 'West Bengal', 'DL': 'Delhi'}
def event_page(request):
    request_slug = request.path[12:]
    e = Event.objects.get(slug = request_slug)
    event_name = e.name
    event_description = e.description
    event_time = e.startTime
    event_state = stateList[e.state]
    event_venue = e.venue
    event_image = e.image
    
    context = {
        'event_name': event_name,
        'event_description': event_description,
        'event_time': event_time,
        'event_state': event_state,
        'event_venue': event_venue,
        'event_image': event_image 
    }
    if request.method == 'POST':
        return register_for_event(request.user, e)
    else:
        return render(request, 'event_page.html', context)

def register_for_event(user_obj, event_obj): 
    if not user_obj.is_authenticated:
        return redirect('login')
    r = Registrations()
    r.user = user_obj
    r.event = event_obj
    r.save()
    return HttpResponse("User is registered for event!")

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,"Registration Successfull!")         
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})

def search_events(request):

    if request.method == 'POST':
        searched = request.POST['searched']
        std = request.POST['state']
        if std=='':
            events = Event.objects.filter(name__icontains=searched)
        else:    
            events = Event.objects.filter(name__icontains=searched).filter(state=stateCodes[std])

        return render(request,
                      'search_events.html',
                      {'searched':searched,
                       'events':events})
             
    else:
         return render(request,'search_events.html',{})
    

# from .models import Alert, State
# def set_alert(request):
#     if request.method == 'POST':
#         state_id = request.POST.get('state')
#         state = State.objects.get(id=state_id)
#         user = request.user
#         alert = Alert.objects.create(state=state, user=user)
#         alert.save()
#         return redirect('success')
#     else:
#         states = State.objects.all()
#     return render(request, 'set_alert.html', {'states': states})
