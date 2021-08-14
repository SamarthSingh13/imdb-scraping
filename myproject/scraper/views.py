from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def index(request):
    movie_list = Movie.objects.order_by('-rating')
    output = [{'Title': x.title,
                'Year': x.year,
                'Rating': x.rating,
                'Thumbnail URL': x.thumbnail_url
                } for x in movie_list]
    return HttpResponse(output)

def display(request,sort_field):
    if not (sort_field in ['title','rating','year']):
        return HttpResponse('Invalid field for sort')
    movie_list = Movie.objects.order_by(sort_field)
    output = [{'Title': x.title,
                'Year': x.year,
                'Rating': x.rating,
                'Thumbnail URL': x.thumbnail_url
                } for x in movie_list]
    return HttpResponse(output)

def search(request,query_title):
    movie = Movie.objects.filter(title=query_title)
    if(len(movie)==0):
        return HttpResponse('Movie not found')
    output = [{'Title': movie[0].title,
                'Year': movie[0].year,
                'Rating': movie[0].rating,
                'Thumbnail URL': movie[0].thumbnail_url}]
    return HttpResponse(output)