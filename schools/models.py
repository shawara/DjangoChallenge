import uuid

from django.db import models


class School(models.Model):
    name = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField()
    location = models.CharField(max_length=127)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "schools"


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="students")
    age = models.PositiveSmallIntegerField()
    nationality = models.CharField(max_length=31)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "students"
