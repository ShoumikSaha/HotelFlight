from django import forms
import datetime

CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)


class SearchHotelForm(forms.Form):
    hoteldest = forms.CharField(label='Hotel or destination place', max_length=100)
    checkin = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    checkout = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    room = forms.CharField(widget=forms.Select(choices=CHOICES))
    adult = forms.CharField(widget=forms.Select(choices=CHOICES))
    children = forms.CharField(widget=forms.Select(choices=CHOICES))
    # checkout = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    # room = forms.IntegerField(label='Room', widget=forms.NumberInput(
    #    attrs={'type': 'range', 'step': '1', 'min': '1', 'max': '10', 'value': '1'}))
    #   children = forms.IntegerField(label='Children', widget=forms.NumberInput(
    #    attrs={'type': 'range', 'step': '1', 'min': '1', 'max': '10', 'value': '0'}))
