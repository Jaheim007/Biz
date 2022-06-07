from django.contrib import admin
from .models import Newsletter, Started, Team, Footer

@admin.register(Newsletter)
class News(admin.ModelAdmin):          
    list_display = ('title', 'description')
    
@admin.register(Team)
class Team(admin.ModelAdmin):           
    list_display = ('section_title', 'name', 'profession')
    
@admin.register(Started)
class Start(admin.ModelAdmin):          
    list_display = ('img', 'title', 'description')
    
@admin.register(Footer)
class Footer(admin.ModelAdmin):        
    list_display = ('title', 'email', 'address', 'phone')

# Register your models here.
