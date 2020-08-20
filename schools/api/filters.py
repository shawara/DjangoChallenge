from django_filters import FilterSet

from schools.models import Student


class StudentsFilter(FilterSet):
    class Meta:
        model = Student
        fields = ['school', 'age', 'nationality']
