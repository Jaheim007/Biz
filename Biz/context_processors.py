from Service.models import Footer

def Footer(request):      
    footer = Footer.objects.get()
    
    return{
        'footer': footer
    }