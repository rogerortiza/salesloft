from rest_framework.routers import DefaultRouter
from people.views import PeopleViewSet

router = DefaultRouter()
router.register(r'people', PeopleViewSet, basename='people')

