from django.urls import path

from .views import DocumentView


app_name = "docs"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('docs/', DocumentView.as_view()),
]
