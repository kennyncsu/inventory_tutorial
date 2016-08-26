"""superstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from inventory import views 

# Django REST Framework
from django.conf.urls import include
from rest_framework import routers

# Django REST Framework router
router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'movies', views.MovieViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^apis/books/list', views.get_available_books),
    url(r'^apis/books/purchase/(?P<id>[0-9])', views.purchase_book),
    url(r'^available_books/(?P<pk>[0-9]+)/$', views.AvailableBookDetail.as_view()),
]
