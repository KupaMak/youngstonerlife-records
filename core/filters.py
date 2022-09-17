from logging import PlaceHolder
from random import choices
from tkinter import filedialog
import django
from django_filters import ChoiceFilter, CharFilter, DateFilter, ModelChoiceFilter
import django_filters
from .models import *


class StudioFilter(django_filters.FilterSet):
    studio_name = CharFilter(field_name='studio_name', lookup_expr='icontains', label='Search By Name')
    location = CharFilter(field_name='location', lookup_expr='icontains', label=' Search By Location')

    class Meta:
        model = Studio
        fields = ['studio_name', 'location']


class StudioSessionFilter(django_filters.FilterSet):
    artist = CharFilter(field_name='artist', lookup_expr='icontains', label='Search By Artist')

    class Meta:
        model = StudioSession
        fields = ['artist']


class AlbumFilter(django_filters.FilterSet):
    album = CharFilter(field_name='album', lookup_expr='icontains', label=False)
    date_released = DateFilter(field_name='date_released', label=False)

    class Meta:
        model = UserAlbum
        fields = ['album', 'date_released', 'artist_id']


class ShowFilter(django_filters.FilterSet):
    artist_id = ModelChoiceFilter(field_name='artist_id', label=False,
                                  queryset=UserDetail.objects.filter(department='Artist'))
    country = CharFilter(field_name='country', lookup_expr='icontains', label=False)
    start_date = DateFilter(field_name='start_date', label=False)

    class Meta:
        model = ShowsTours
        fields = ['country', 'artist_id', 'start_date']


class UserPayrollFilter(django_filters.FilterSet):

    class Meta:
        model = UserPayroll
        fields = ['month', 'artist_id']
