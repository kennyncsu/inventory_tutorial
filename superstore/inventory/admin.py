from django.contrib import admin
from .models import Book 
from .models import Game
from .models import Movie 

# Register your models here.

class InventoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'description', 'special_description',
		'quantity', 'current_price', 'sale_discount', 'cost', 
		'current_profit_margin', 'active']

	def current_profit_margin(self, obj):
		return "%.2f" % obj.profit_margin()

class BookAdmin(InventoryAdmin):
	pass

class GameAdmin(InventoryAdmin):
	pass

class MovieAdmin(InventoryAdmin):
	pass

admin.site.register(Book, BookAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Movie, MovieAdmin)


