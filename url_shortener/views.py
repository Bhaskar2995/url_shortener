from django.views import View
from django.http import JsonResponse
import json
from django.shortcuts import redirect
from .models import Url

#To generate Random string for Short Url
import string
import random

class Home(View):
    """
    This is a class based view which has four methods: get, post, delete, and put.
    """
     
    def get(self, request, *args, **kwargs):
        """
        This method handles GET requests to the given url.
        --> If the URL contains a short URL, it redirects the user to the corresponding long URL. 
        --> If the short URL does not exist, it returns a JSON response with an error message.
        --> If there is no short URL in the URL, it returns a JSON response with a welcome message.
        """

        if 'url' in kwargs:
            try:
                url = Url.objects.get(short_url = kwargs['url'])
                return redirect(url.long_url)
            except:
                message = "Short Url Doesnot match. Please create short url using POST method"
                return JsonResponse(message,safe=False)
        return JsonResponse('Welcome to URL shortener website', safe= False)
    
    def post(self, request, *args, **kwargs):
        """
        This method handles POST requests to the given url.
        --> It expects a JSON payload with a "long_url" key that contains the long URL to be shortened. It saves the short_url into the database
        --> If a short URL already exists for the given long URL, it returns a JSON response with the existing short URL.
        """
         
        data = json.loads(request.body)
        long_url  = data.get('long_url')
        N = 7
        try:
            url = Url.objects.get(long_url=long_url)
            message = "The short url already exist for the given link. The short url is %s" %url.short_url
            return JsonResponse(message,safe=False)
        except:
            short_url = ''.join(random.choices(string.ascii_letters, k=N))
            url = Url(long_url = long_url, short_url = short_url)
            url.save()
        data = {'long_url': url.long_url, 'short_url': url.short_url}
        return JsonResponse(data)
    
    def delete(self, request, *args, **kwargs):
        """
        This method handles DELETE requests for the given link.
        --> If the URL contains a short URL, it deletes the corresponding URL from the database and returns a JSON response with a success message. 
        --> If the short URL does not exist, it returns a JSON response with an error message.
        """

        if 'url' in kwargs:
            try:
                url = Url.objects.get(short_url = kwargs['url'])
                url.delete()
                message = "The Short Url has been deleted successfully"
                return JsonResponse(message,safe=False)
            except:
                message = "Short Url Doesnot match. Please create short url using POST method"
                return JsonResponse(message,safe=False)
            
    def put(self,request, *args, **kwargs):
        """
        This method handles PUT requests for the given link.
        --> If the URL contains a short URL, it expects a JSON payload with a "long_url" key that contains the new long URL. 
        --> It updates the corresponding URL in the database and returns a JSON response with a success message. 
        --> If the short URL does not exist, it returns a JSON response with an error message.
        """

        if 'url' in kwargs:
            try:
                data = json.loads(request.body)
                long_url  = data.get('long_url')
                short_url = kwargs['url']
                url = Url.objects.get(short_url = short_url)
                url.long_url = long_url
                url.save()
                message = "The Short Url has been updated successfully"
                return JsonResponse(message,safe=False)
            except:
                message = "Short Url Doesnot match. Please create short url using POST method"
                return JsonResponse(message,safe=False)
        else:
            message = "Format you entered is wrong. The correct format is localhost:8000/{short_url}"
            return JsonResponse(message, safe=True)