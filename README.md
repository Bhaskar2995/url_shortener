# URL Shortener
This is a simple project which allows you to generate short URL for any given long URL.

# Tech Stack Used
1. Python (version=3.10.5)
2. Django (version = 4.2)

# Endpoints 

EndPoint | HTTP Request | Request Body | Result | Example URL
--- | --- | --- | --- |---
/ | GET | Blank | Returns a "Welcome to URL shortener website" string | http://localhost:8000/
/{url} | POST | "long_url": "{long_url}" | {"long_url": "{long_url}", "short_url": "{generated short_url}" }  | localhost:8000/url 
/{generated short url} | GET | Blank | It gets redirected to the original URL  | localhost:8000/HuWCBGJ
/{generated short url} | PUT | "long_url": "{long_url}" | "The Short Url has been updated successfully"  | localhost:8000/HuWCBGJ
/{generated short url} | DELETE | Blank | "The Short Url has been deleted successfully"  | localhost:8000/HuWCBGJ
