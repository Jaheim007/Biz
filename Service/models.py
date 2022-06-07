from django.db import models

class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
class Started(models.Model): 
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.FileField()
    
class Team(models.Model):     
    section_title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    fb_link = models.URLField()
    Insta_link = models.URLField()
    Linked_link = models.URLField()
    
class Footer(models.Model):   
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    fb_link = models.URLField()
    youtude_link = models.URLField()
    twitter_link = models.URLField()
    insta_link = models.URLField()
    linked_link = models.URLField()   
    
    
    
    
# Create your models here.
