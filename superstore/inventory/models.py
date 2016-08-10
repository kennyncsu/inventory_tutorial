from django.db import models

# Create your models here.

class Item(models.Model):

	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	quantity = models.IntegerField()
	current_price = models.DecimalField(decimal_places=2, max_digits=5)
	sale_discount = models.IntegerField(default=0)
	cost = models.DecimalField(decimal_places=2, max_digits=5)
	active = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	def profit_margin(self):
		return self.current_price - (self.current_price * self.sale_discount / 100) - self.cost

	class Meta:
		abstract = True

class Book(Item):
	BOOK_CHOICES = (
		('Hardcover', 'Hardcover'),
		('Paperback', 'Paperback')
		)

	special_description = models.CharField(max_length=15, 
		choices=BOOK_CHOICES)

class Game(Item):
	GAME_CHOICES = (
		('Nintendo Wii U', 'Nintendo Wii U'),
		('Playstation 4', 'Playstation 4'),
		('Xbox One', 'Xbox One')
		)

	special_description = models.CharField(max_length=15,
		choices=GAME_CHOICES)

class Movie(Item):
	MOVIE_CHOICES = (
		('Blu-ray', 'Blu-ray'),
		('DVD', 'DVD'),
		('VHS', 'VHS')
		)

	special_description = models.CharField(max_length=15,
		choices=MOVIE_CHOICES)



