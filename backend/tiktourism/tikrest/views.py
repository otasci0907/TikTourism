from django.contrib.gis.geoip2 import GeoIP2
from tikrest.models import Restaurant
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from decouple import config
import geopy.distance
import requests
import time

def index(request):
    API_KEY = config('GOOGLE_API')

    request.session = {}

    g = GeoIP2() 
    ip = request.META.get('REMOTE_ADDR', None)
    lat,lng = g.lat_lon("74.106.235.255")
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(lat) + "%2C" + str(lng) + "&radius=1500&type=restaurant&key=" + API_KEY

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    for place in response.json()["results"]:
        name = place["name"]
        rating = place["rating"]
        try:
            loc = Restaurant.objects.get(name=name, rating=rating)
        except Restaurant.DoesNotExist:
            loclat = place["geometry"]["location"]["lat"]
            loclng = place["geometry"]["location"]["lng"]
            prox = geopy.distance.geodesic((lat,lng), (loclat, loclng)).mi
            mil = True;
            if (prox * 2252 <= 1000):
                prox = prox * 2252
                mil = False
            else:
                prox = round(prox, 3)
            element = place["photos"][0]["photo_reference"]
            photo_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference=" + element + "&key=" + API_KEY

            payload={}
            headers = {}

            imageResponse = requests.request("GET", photo_url, headers=headers, data=payload)
            loc = Restaurant(name=name, rating=rating, image=imageResponse.url, time_spent=0.0, proximity=prox, prox_mi=mil, liked=False, clicked=False)
            loc.save()

    restaurants = Restaurant.objects.all().values()
    context = {
        "restaurants": restaurants.order_by('proximity').values(),
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def restaurantUpdate(request, name, rating, prox):
    restaurant = Restaurant.objects.get(name=name, rating=rating, proximity=prox)
    restaurant.clicked = True
    restaurant.save()
    request.session = {
        'name': restaurant.name,
        'rating': restaurant.rating,
        'proximity': restaurant.proximity,
        'image': restaurant.image,
    }
    print(request.session.keys())
    return redirect('restaurant')

def restaurant(request):
    template = loader.get_template('restaurant.html')
    print(request.session.keys())
    context = {}
    return HttpResponse(template.render(context, request))

def updaterecord(request, name, rating, prox):
    time = request.POST['time']
    member = Restaurant.objects.get(name=name, rating=rating, proximity=prox)
    member.time_spent = float(time) + member.time_spent
    member.save()
    return HttpResponseRedirect(reverse('index'))

def updatelike(request, name, rating, prox):
    member = Restaurant.objects.get(name=name, rating=rating, proximity=prox)
    member.liked = not member.liked;
    member.save()
    return HttpResponseRedirect(reverse('index'))