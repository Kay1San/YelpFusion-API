from django import forms

class YelpSearchForm(forms.Form):
    termFood = forms.CharField(label='Search Yelp', max_length=100)
    address = forms.CharField(label='Location', max_length=100)