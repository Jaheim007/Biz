from django.db import models

class Banner(models.Model):        
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.FileField()

class About(models.Model):       
    title = models.CharField(max_length=255)
    description = models.TextField()
    mini_title1 = models.CharField(max_length=255)
    mini_description1 = models.TextField()
    mini_title2 = models.CharField(max_length=255)
    mini_description2 = models.TextField()
    img = models.FileField()
    
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
    section_title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    
    
    
    

    
# Create your models here.
