from .models import Book 
from .models import Game
from .models import Movie 
from rest_framework import serializers

class BookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Book
		fields = ('url', 'name', 'description', 'quantity', 'sale_discount', 
			'cost', 'active', 'special_description')

class GameSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Book
		fields = ('url', 'name', 'description', 'quantity', 'sale_discount', 
			'cost', 'active', 'special_description')

class MovieSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Book
		fields = ('url', 'name', 'description', 'quantity', 'sale_discount', 
			'cost', 'active', 'special_description')
