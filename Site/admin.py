from pyexpat import model
from django.contrib import admin
from .models import Banner, About, Features, Features_Details, Slider, Testimonial

@admin.register(Banner)
class Banner(admin.ModelAdmin):      
    list_display = ('img','title', 'description')
    
@admin.register(About)
class About(admin.ModelAdmin):        
    list_display = ('img','title', 'description',)
    
@admin.register(Features)
class Feature(admin.ModelAdmin):         
    list_display = ('title', 'description')
    
@admin.register(Features_Details)
class Features_Detail(admin.ModelAdmin):
    list_display = ('img','title', 'description' )
    
@admin.register(Slider)
class Slider(admin.ModelAdmin):     
    list_display = ('img',)
    
@admin.register(Testimonial)
class Testimonial(admin.ModelAdmin):          
    list_display = ('section_title', 'description', 'client_name', 'profession')







# Register your models here.
