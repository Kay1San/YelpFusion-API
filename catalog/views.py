from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import requests
from .forms import YelpSearchForm
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse
from django.conf import settings


# Create your views here.
def yelp_query(keyword, location):
  YELP_URL = 'https://api.yelp.com/v3/businesses/search'

  headers = {'Authorization': 'Bearer %s' % settings.YELP_API_KEY}
  params = {'term': keyword, 'location': location}
  query = requests.get(YELP_URL, params=params, headers=headers)
  return query.json()


def reviews_query(business_id):
   YELP_URL = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(business_id)
   headers = {'Authorization': 'Bearer %s' % settings.YELP_API_KEY}
   query = requests.get(YELP_URL, headers=headers)
   return query.json()


def business_details_query(business_id):
   YELP_URL = 'https://api.yelp.com/v3/businesses/{}'.format(business_id)
   headers = {'Authorization': 'Bearer %s' % settings.YELP_API_KEY}
   query = requests.get(YELP_URL, headers=headers)
   return query.json()


def search_result(request):
  items = []
  food = request.GET.get('term') #Ex in url term = pizza
  location = request.GET.get('location') #Ex in url location = Montreal
  if food:
    businesss_data = yelp_query(keyword=food, location=location)
    biz_count = len(businesss_data["businesses"])

    for i in range(biz_count):
       review_data = reviews_query(businesss_data["businesses"][i]["id"]) #COMMENTED SINCE ITS USES A LOT OF API DATA (500 LIMIT)

       items.append({
                "business_info": businesss_data["businesses"][i],
                "term":food,
                "location":location,
                "reviews": review_data["reviews"][0]["text"] 
            })
    

    return render(request, 'search.html', {'items': items})
  
  return render(request, 'search.html', {'items': items})



def get_business_details(request, business_id):
   
  details = business_details_query(business_id)

  context = {
       "name": details["name"],
       "url": details["url"],
       "photos": details["photos"]
    }

  return render(request, 'details.html', context)


def autocomplete(request):
    term = request.GET.get('term', '')
    response = requests.get(
        'https://api.yelp.com/v3/autocomplete',
        headers={'Authorization': 'Bearer %s' % settings.YELP_API_KEY},
        params={'text': term}
    )

    yelp_response = response.json()
    terms = yelp_response.get('terms', [])
    terms_text = [term['text'] for term in terms]

    # Return only the text data as a JSON response
    return JsonResponse({'terms': terms_text})



   
class HomePageView(TemplateView):
    template_name = 'home.html'


            
