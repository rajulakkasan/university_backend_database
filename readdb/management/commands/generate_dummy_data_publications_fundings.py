import random
from faker import Faker
from readdb.models import Instructor, Publication, FundingSecured

fake = Faker()

from django.core.management.base import BaseCommand
from readdb.models import Student, Instructor, User

class Command(BaseCommand):
    help = 'Populate user data into publications and fundingsecured models'

    def handle(self, *args, **kwargs):
        self.generate_publications_and_funding()

    def generate_publications_and_funding(self):
        try:
        
            instructors = Instructor.objects.all()
            semesters = [1, 2]
            for instructor in instructors:
                # Generate random number of publications
                num_publications = random.randint(1, 5)
                for _ in range(num_publications):
                    publication = Publication.objects.create(
                        instructor=instructor,
                        title=fake.sentence(nb_words=5),
                        publication_year=random.randint(2019, 2020),
                        semester=random.choice(semesters)
                    )
                    self.stdout.write(self.style.SUCCESS(f"Created Instructor Publication: {publication}"))
                
                # Generate random funding secured
                num_fundings = random.randint(1, 3)
                for _ in range(num_fundings):
                    funding = FundingSecured.objects.create(
                        instructor=instructor,
                        amount=random.randint(10000, 50000),
                        academic_year=random.randint(2019, 2020),
                        semester=random.choice(semesters)
                    )
                    self.stdout.write(self.style.SUCCESS(f"Created Instructor Funding Secured : {funding}"))

        except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Error creating : {e}"))