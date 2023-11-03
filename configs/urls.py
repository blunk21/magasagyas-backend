from django.urls import path
from . import views

urlpatterns = [
    path("configs/", views.ConfigsView.as_view()),
    path("configs/<int:id>/", views.ConfigsView.as_view()),
    path("create_new_config/",views.create_new_config,name="create_new_config")
]
