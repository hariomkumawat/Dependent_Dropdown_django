from django.shortcuts import render
from .models import Country, State, City
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json

# Create your views here.
def index(request):
    countries = Country.objects.values('id','name')
    return render(request,"dropdown.html",{'countries':countries})

def fetch_state(request):
    country_id = request.POST.get('country_id')
    states = list(State.objects.filter(country_id=country_id).values('name','id'))
    return JsonResponse({'states':states},safe=False)

def fetch_city(request):
    state_id = request.POST.get('state_id')
    cities = list(City.objects.filter(state_id=state_id).values('name','id'))
    return JsonResponse({'cities':cities},safe=False)