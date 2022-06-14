from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Newsletter, Started, Footer, TeamMember, Sevice_details, Contact

@admin.register(Newsletter)
class News(admin.ModelAdmin):          
    list_display = ('Email', )

@admin.register(Contact)
class Contact(admin.ModelAdmin):          
    list_display = ('name','email' )
    
    
@admin.register(TeamMember)
class TeamMember(admin.ModelAdmin):           
    list_display = ('views','name',)

    def views(self, obj):     
        return mark_safe(f'<img src="{obj.img.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images' 

    
@admin.register(Started)
class Start(admin.ModelAdmin):          
    list_display = ('views', 'description')

    
    def views(self, obj):     
        return mark_safe(f'<img src="{obj.img.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images'
    
    
@admin.register(Footer)
class Footer(admin.ModelAdmin):        
    list_display = ('title', 'email', 'address', 'phone')

@admin.register(Sevice_details)
class Service(admin.ModelAdmin):        
    list_display = ('title', 'description', 'img1', 'img2')

# Register your models here.
