from django.urls import path

from schools.api.v1 import views

urlpatterns = [
    path('schools/', views.SchoolsModelViewSet.as_view({"get": "list", "post": "create"})),
    path('schools/<int:pk>/', views.SchoolsModelViewSet.as_view(
        {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"})),
    path('students/', views.StudentsModelViewSet.as_view({"get": "list", "post": "create"})),
    path('students/<uuid:pk>/', views.StudentsModelViewSet.as_view(
        {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"})), ]
