import email
from django.shortcuts import render, redirect
from .models import Banner, About, AboutDetails, Features_Details, Site_Info, Slider, Testimonial 
from Service.models import Newsletter, Started, Sevice_details, TeamMember, Newsletter, Social_Team


def index(request):   
    banner = Banner.objects.all()  
    about = About.objects.all()  
    about_details = AboutDetails.objects.all()
    Start = Started.objects.all()
    features_details = Features_Details.objects.all()
    img = Slider.objects.all()
    section = Site_Info.objects.first()
    service = Sevice_details.objects.all()
    testimonial = Testimonial.objects.all()
    team = TeamMember.objects.all() 
    social_team = Social_Team.objects.all()     
    
    if request.method == "POST":
        email = request.POST['email']
        news = Newsletter(email = email)
        news.save()
            
    return render(request, 'pages/index.html', locals())

    
def about(request):  
    about_details = AboutDetails.objects.all()     
    features_details = Features_Details.objects.all()
    team = TeamMember.objects.all() 
    about = About.objects.all() 
    section = Site_Info.objects.first()

    return render(request, 'pages/about.html', locals())

def error(request): 
    section = Site_Info.objects.first()      
    return render(request, 'pages/404.html', locals())

def contact(request):  
    section = Site_Info.objects.first()     
    return render(request, 'pages/contact.html', locals())

def feature(request):   
    features_details = Features_Details.objects.all()  
    section = Site_Info.objects.first()  
    return render(request, 'pages/feature.html', locals())

def quote(request):  
    section = Site_Info.objects.first()   
    
    if request.method == "POST":  
        name = request.POST['name']  
        email = request.POST['email']
        news = Newsletter(email = email)
        news.save()   
          
    return render(request, 'pages/quote.html', locals())

def team(request): 
    team = TeamMember.objects.all() 
    section = Site_Info.objects.first()      
    return render(request, 'pages/team.html', locals())

def testimonial(request):      
    testimonial = Testimonial.objects.all()  
    section = Site_Info.objects.first()
    return render(request, 'pages/testimonial.html', locals())

def service(request):   
    service = Sevice_details.objects.all()  
    testimonial = Testimonial.objects.all()  
    section = Site_Info.objects.first()
    return render(request, 'pages/service.html', locals())



# Create your views here.
