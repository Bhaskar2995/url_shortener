from django.views import View
from django.http import JsonResponse
import json
from django.shortcuts import redirect
from .models import Url

#To generate Random string for Short Url
import string
import random



class Home(View):
    def get(self, request, *args, **kwargs):
        if 'url' in kwargs:
            try:
                url = Url.objects.get(short_url = kwargs['url'])
                return redirect(url.long_url)
            except:
                message = "Short Url Doesnot match. Please create short url using POST method"
                return JsonResponse(message,safe=False)
        return JsonResponse('Welcome to url shortener', safe= False)
    
    def post(self, request, *args, **kwargs):
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