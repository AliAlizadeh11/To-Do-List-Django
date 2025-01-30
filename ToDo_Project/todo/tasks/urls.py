from rest_framework.routers import DefaultRouter
from .views import TodoView

router = DefaultRouter()
router.register('todo', TodoView, basename='data')
urlpatterns = router.urls
