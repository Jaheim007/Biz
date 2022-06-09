from pyexpat import model
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import AboutDetails, Banner, About, Features, Features_Details, Slider, Testimonial, TestTitle

@admin.register(Banner)
class Banner(admin.ModelAdmin):      
    list_display = ('views','title', 'description')

    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.img.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images'
    
@admin.register(About)
class About(admin.ModelAdmin):        
    list_display = ('views','title', 'description',)

    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.img.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images'

@admin.register(AboutDetails)
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
    list_display = ('views',)

    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.img.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images'
    
@admin.register(Testimonial)
class Testimonial(admin.ModelAdmin):          
    list_display = ( 'views', 'client_name', 'profession')

    def views(self, obj):     
        return mark_safe(f'<img src="{obj.img.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images'
    
@admin.register(TestTitle)
class Test(admin.ModelAdmin):          
    list_display = ( 'section_title', )







# Register your models here.
