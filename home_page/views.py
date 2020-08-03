from django.shortcuts import render

# Create your views here.
def home_page(request):
    mapbox_access_token = 'pk.eyJ1IjoiYW55dXNlcm5hbWUiLCJhIjoiY2tkZGgyaHBxMGM0dTJxbnJsZjJzenAybCJ9.0msTET9V9ZehzJqfK55u3A'
    return render(request, 'home_page/index.html', {'mapbox_access_token':mapbox_access_token})
