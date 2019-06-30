from django import forms
import datetime


class SearchHotelForm(forms.Form):
    hoteldest = forms.CharField(label='Hotel or destination place', max_length=100)
    checkin = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    #checkout = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    #room = forms.IntegerField(label='Room', widget=forms.NumberInput(
    #    attrs={'type': 'range', 'step': '1', 'min': '1', 'max': '10', 'value': '1'}))
    #adult = forms.IntegerField(label='Adult', widget=forms.NumberInput(
    #    attrs={'type': 'range', 'step': '1', 'min': '1', 'max': '10', 'value': '2'}))
    #children = forms.IntegerField(label='Children', widget=forms.NumberInput(
    #    attrs={'type': 'range', 'step': '1', 'min': '1', 'max': '10', 'value': '0'}))
