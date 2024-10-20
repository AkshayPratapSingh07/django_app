from rest_framework import routers

from .api_views import QuestionViewSet,ChoiceViewSet

router = routers.DefaultRouter()
router.register(r"questions", QuestionViewSet)
router.register(r"choice", ChoiceViewSet)


urlpatterns = router.urls
