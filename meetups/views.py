from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

# Func for starting page/index
def index(request):    
    meetups = [
        { 
            'title' : 'A First Meetup', 
            'location':'New York', 
            'slug': 'a-first-meetup'
        },
        { 
            'title' : 'A Second Meetup', 
            'location':'Chicago', 'slug': 
            'a-second-meetup'
        },
        {
            'title' : 'A Third Meetup', 
            'location':'New Orleans', 
            'slug': 'a-third-meetup'
        },
    ]
    
    # Need to return response to browser for homepage
    # render will config a template into an HttpResponse
    # render needs 2 args: req  uest, then relative path to template 
    # Optional 3rd arg: dict of key/vals to inject into template
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })
    
    # Simple return of HttpResponse
    # return HttpResponse("Hello Hope!")