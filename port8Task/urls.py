from django.urls import path, include

from battle import views
from battle.views import BattleViewset
from captain.views import CaptainViewSet
from rest_framework.routers import DefaultRouter
from ship.views import ShipViewSet

router = DefaultRouter()
router.register(r'ships', ShipViewSet, basename='ship')
router.register(r'captain', CaptainViewSet)
router.register(r'battles', BattleViewset)

urlpatterns = [
     path('', include(router.urls)),
]
