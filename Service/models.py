from django.db import models

class Newsletter(models.Model):
   Email = models.EmailField( max_length=254)
    
class Started(models.Model): 
    description = models.TextField()
    img = models.FileField()

class Sevice_details(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img1 = models.CharField(max_length=255)
    img2 = models.CharField(max_length=255)


class TeamMember(models.Model):       
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    img = models.FileField()
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
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    
    
    
# Create your models here.
