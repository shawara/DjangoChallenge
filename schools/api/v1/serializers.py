from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext as _

from schools.models import Student, School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'capacity', 'location')
        read_only_fields = ('id',)
        model = School


class StudentSerializer(serializers.ModelSerializer):
    def validate_school(self, school):
        if school.students.count() >= school.capacity:
            # new student or existing student moving to a full capacity school
            if self.instance is None or self.instance.school_id != school.id:
                raise ValidationError(_("School is already full capacity"))
        return school

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'school', 'age', 'nationality')
        read_only_fields = ('id',)
        model = Student
