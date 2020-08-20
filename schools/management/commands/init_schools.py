from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Student, School


class Command(BaseCommand):

    def handle(self, *args, **options):
        fake = Faker()

        if School.objects.count() == 0:
            schools = School.objects.bulk_create(
                [School(name=fake.first_name()[:20], capacity=fake.random_int(10, 40), location=fake.city()) for _ in
                 range(12)]
            )
            students = []
            for school in schools:
                students.extend(
                    [Student(school=school, first_name=fake.first_name()[:20], last_name=fake.last_name()[:20],
                             nationality=fake.country()[:31], age=fake.random_int(10, 18))
                     for _ in range(fake.random_int(10, school.capacity))])

            Student.objects.bulk_create(students)
