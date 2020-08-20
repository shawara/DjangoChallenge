from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .serializers import SchoolSerializer, StudentSerializer
from ..filters import StudentsFilter
from ...models import School, Student


class SchoolsModelViewSet(ModelViewSet):
    filter_backends = (SearchFilter, OrderingFilter)
    ordering_fields = ['name', 'capacity']
    search_fields = ['name']
    serializer_class = SchoolSerializer
    queryset = School.objects.all().order_by('pk')


class StudentsModelViewSet(ModelViewSet):
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    ordering_fields = ['first_name', 'last_name', 'age', 'nationality']
    search_fields = ['first_name', 'last_name']
    filter_class = StudentsFilter
    serializer_class = StudentSerializer
    queryset = Student.objects.all().order_by('pk')
