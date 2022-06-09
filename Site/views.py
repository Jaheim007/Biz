from django.shortcuts import render
from .models import Banner, About, AboutDetails, Features_Details
from Service.models import Newsletter, Started

def index(request):     
    banner = Banner.objects.all()  
    about = About.objects.all()  
    about_details = AboutDetails.objects.all()
    Start = Started.objects.all()
    features_details = Features_Details.objects.all()
    return render(request, 'pages/index.html', locals())

def about(request):       
    return render(request, 'pages/about.html', locals())

def error(request):       
    return render(request, 'pages/404.html', locals())

def contact(request):       
    return render(request, 'pages/contact.html', locals())

def feature(request):       
    return render(request, 'pages/feature.html', locals())

def quote(request):       
    return render(request, 'pages/quote.html', locals())

def team(request):       
    return render(request, 'pages/team.html', locals())

def testimonial(request):       
    return render(request, 'pages/testimonial.html', locals())

def service(request):       
    return render(request, 'pages/service.html', locals())



# Create your views here.
