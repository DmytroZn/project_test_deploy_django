from django.urls import path

from . import views

urlpatterns = [
    path('', views.Move.as_view()),
    # path('huston_1'pyth)
]