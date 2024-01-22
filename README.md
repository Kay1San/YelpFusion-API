# Yelp Clone Web Application

This is an work in progress project in which I'm recreating Yelp's website with Django and Python, while also planning to add new features such as time-based review score plots


## Requirements

This project requires an API key for both Yelp Fusion API and Google Places API in which you can register below

* [Yelp Fusion API](https://docs.developer.yelp.com/docs/fusion-authentication)
* [Google Places API](https://developers.google.com/maps/documentation/places/web-service/get-api-key)

## Installation

The first step to set up this project on your local machine is to clone this repository
```
https://github.com/Kay1San/YelpFusion-API.git
``` 

Once the repository is cloned, install the following dependencies 

``` 
pip install django
pip install python-dotenv
pip install requests
``` 

Since Django uses a SECRET_KEY, type this command on your terminal
```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
``` 
 
Create a .env file in the root directory of the app by following the instructions inside example.env

Apply the migrations once everything is completed

```
python manage.py migrations
```

## Instructions

Run the app locally with the command
```
python manage.py runserver
```

Here's how the home page looks like so far, it features the autocomplete packages from @trevoreyre

![home page](./catalog/static/home-page.png)


![results page](./catalog/static/search-results.png)

## Documentations

* [Django Documentation](https://docs.djangoproject.com/en/5.0/)
* [Yelp Fusion Documentation](https://docs.developer.yelp.com/docs/fusion-intro)
* [Google Places Documentation](https://developers.google.com/maps/documentation/places/web-service/overview)
* [Autocomplete package](https://autocomplete.trevoreyre.com/#/)



