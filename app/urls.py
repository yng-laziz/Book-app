from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'authors', AutorView)
router.register(r'books', BookView)
router.register(r'categories', CategoriesView)


urlpatterns = [
    path('', include(router.urls))
]
