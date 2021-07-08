from django.urls import path

from .views import DocumentView
from . import views

app_name = "docs"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('docs/', DocumentView.as_view()),
    path('management/', views.management, name='management'),
]
