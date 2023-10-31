from django.urls import path
from . import views

urlpatterns = [
    path("message/",views.ModuleMessagesView.as_view())
]