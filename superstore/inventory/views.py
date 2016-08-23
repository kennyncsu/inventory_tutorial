from django.shortcuts import render
from .models import Book
from .models import Game
from .models import Movie
from django.http import HttpResponse

import json

# Django REST Framework imports
from rest_framework import viewsets
from .serializers import BookSerializer
from .serializers import GameSerializer
from .serializers import MovieSerializer
# end imports

# Create your views here.

def get_available_books(request): 
	if request.method == 'GET':
		books = []

		for book in Book.objects.filter(active=True, quantity__gt=0).order_by('name'):
			books.append(str(book))

		return HttpResponse(json.dumps(books), content_type='text/json',
			status=200)
	else: 
		return HttpResponse(json.dumps('Forbidden'), content_type='text/json', 
			status=403)


def purchase_book(request, id):
	if request.method == 'GET': # easy to test a GET, but should be a POST
		book = Book.objects.get(id=id)

		if book.active and book.quantity > 0: 
			# purchase it
			book.quantity = book.quantity - 1
			book.save()

			return HttpResponse(json.dumps('Purchased'), content_type='text/json',
				status=200)

		else: 
			return HttpResponse(json.dumps('Not Available'), content_type='text/json',
				status=404) 

	else:
		return HttpResponse(json.dumps('Forbidden'), content_type='text/json',
			status=403) 


# Django REST Framework views below 

class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all().order_by('name')
	serializer_class = BookSerializer

class GameViewSet(viewsets.ModelViewSet):
	queryset = Game.objects.all().order_by('name')
	serializer_class = GameSerializer

class MovieViewSet(viewsets.ModelViewSet):
	queryset = Movie.objects.all().order_by('name')
	serializer_class = MovieSerializer





