from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import DataUpdateViewSet
from .views import PlanetViewSet
from .views import CharacterViewSet
from .views import PlanetPeopleViewSet



from . import views

router = DefaultRouter()
router.register(r'dataupdate', DataUpdateViewSet, basename='dataupdate')
router.register(r'people', CharacterViewSet, basename='people')
router.register(r'planets', CharacterViewSet, basename='planets')
router.register(r'population', CharacterViewSet, basename='population')



urlpatterns = router.urls

app_name = "docs"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('planets/', PlanetViewSet.as_view({'get': 'list'})),
    path('planets/<int:pk>/', PlanetViewSet.as_view({'get': 'retrieve'})),
    path('population/<int:pk>/', PlanetPeopleViewSet.as_view({'get': 'list'})),
    path('people/', CharacterViewSet.as_view({'get': 'list'})),
    path('people/<int:pk>/', CharacterViewSet.as_view({'get': 'retrieve'})),
    path('dataupdate/', DataUpdateViewSet.as_view({'get': 'list'})),
    path('management/', views.management, name='management'),
]
