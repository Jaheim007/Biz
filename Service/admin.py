from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Newsletter, Started, Team, Footer, TeamMember

@admin.register(Newsletter)
class News(admin.ModelAdmin):          
    list_display = ('title', 'description')
    
@admin.register(Team)
class Team(admin.ModelAdmin):           
    list_display = ('section_title',)
    
@admin.register(TeamMember)
class TeamMember(admin.ModelAdmin):           
    list_display = ('views','name',)

    def views(self, obj):     
        return mark_safe(f'<img src="{obj.img.url}" style = "height:100px; width:200px">')
    views.short_description =  'Aperçu des images' 

    
@admin.register(Started)
class Start(admin.ModelAdmin):          
    list_display = ('img', 'title', 'description')
    
@admin.register(Footer)
class Footer(admin.ModelAdmin):        
    list_display = ('title', 'email', 'address', 'phone')

# Register your models here.
