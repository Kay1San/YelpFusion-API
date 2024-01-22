from django.urls import path
from . import views
from .views import HomePageView

# URL Configurations
urlpatterns = [
    #Example of search : http://127.0.0.1:8000/results/?term=pizza&location=Montreal
    path('results/', views.search_result, name='search_yelp'),
    path("", HomePageView.as_view(), name="home"),
    #example  of autocomplete : http://127.0.0.1:8000/autocomplete/?term=pizza which returns {"categories": [{"alias": "pizza", "title": "Pizza"}], "businesses": [], "terms": [{"text": "Pizza Near Me"}, {"text": "Pizza Hut"}, {"text": "Pizza Delivery"}]}
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    path('biz/<str:business_id>', views.get_business_details, name='business_details')
]