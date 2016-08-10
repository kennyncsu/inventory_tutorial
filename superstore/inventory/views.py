from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

import json

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
	pass





