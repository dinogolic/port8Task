from django.urls import path, include

from battle import views
from battle.views import BattleViewset
from rest_framework.routers import DefaultRouter
from ship.views import ShipViewSet

router = DefaultRouter()

router = router.register(r'battles', BattleViewset)
router.register(r'simuliraj_napad', BattleViewset, basename='simuliraj_napad')
router.register(r'zavrsi_bitku', BattleViewset, basename='zavrsi_bitku')
urlpatterns = router.urls
