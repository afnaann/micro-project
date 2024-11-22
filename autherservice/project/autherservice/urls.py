from django.urls import path

from .views import AutherBooks

urlpatterns = [
    path('post/',AutherBooks.as_view())
]
