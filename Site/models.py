from django.db import models

class Banner(models.Model):        
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.FileField() 

class TestTitle(models.Model):
    section_title = models.CharField(max_length=255)  

class About(models.Model):       
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.FileField()

class AboutDetails(models.Model):
    title =  models.CharField(max_length=255)
    description = models.TextField()
    img = models.CharField(max_length=255)
    
class Features(models.Model):      
    title = models.CharField(max_length=255)
    description = models.TextField()
    
class Features_Details(models.Model):      
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.CharField(max_length=255)
    
class Slider(models.Model):     
    img = models.FileField()
    
class Testimonial(models.Model):       
    description = models.TextField()
    client_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    img = models.FileField() 
    
    
    

    
# Create your models here.
