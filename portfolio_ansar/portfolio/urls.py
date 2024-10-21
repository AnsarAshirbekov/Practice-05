from django.urls import path, include
from .views import index, skills, portfolio

urlpatterns = [
    path('', index, name='about_me'),
    path('skills', skills, name='skills'),
    path('portfolio', portfolio, name='portfolio')
]