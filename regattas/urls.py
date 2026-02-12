from django.urls import path, include
from rest_framework.routers import DefaultRouter
from  .views import RegattaViewSet, ResultViewSet, RaceViewSet, ClubViewSet
from . import views

"""
registering  ViewSets so they get URLS
"""

router = DefaultRouter()
router.register(r'regattas', RegattaViewSet)
router.register(r'results', ResultViewSet)
router.register(r'races', RaceViewSet)
router.register('clubs', ClubViewSet)


urlpatterns = [
    path("", views.index, name="index"),
    path('api/', include(router.urls)),
]
