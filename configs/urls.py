from django.urls import path
from . import views

urlpatterns = [
    path("configs/<int:id>/", views.ConfigsView.as_view()),
]
