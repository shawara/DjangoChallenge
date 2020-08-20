from django.urls import path, include
from rest_framework_nested import routers
from .views import StudentsModelViewSet, SchoolsModelViewSet

router = routers.SimpleRouter()
router.register(r'schools', SchoolsModelViewSet)

domains_router = routers.NestedSimpleRouter(router, r'schools', lookup='school')
domains_router.register(r'students', StudentsModelViewSet, basename='school-students')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(domains_router.urls)),
]
