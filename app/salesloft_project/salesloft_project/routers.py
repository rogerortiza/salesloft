from rest_framework.routers import SimpleRouter
from people.views import PeopleViewSet, PeopleCountUniqueCharViewSet

router = SimpleRouter()
router.register(r'people', PeopleViewSet, basename='people')
router.register(r'people-unique-character', PeopleCountUniqueCharViewSet, basename='people-unique-character')
