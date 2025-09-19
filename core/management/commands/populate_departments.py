from django.core.management.base import BaseCommand
from core.models import SubjectTag

class Command(BaseCommand):
    help = 'Populate subjects with department information'

    def handle(self, *args, **options):
        # Sample departments and subjects
        department_subjects = {
            'Computer Science': [
                'CS101 - Introduction to Programming',
                'CS201 - Data Structures',
                'CS301 - Algorithms',
                'CS401 - Software Engineering',
                'CS501 - Database Systems',
                'CS601 - Machine Learning',
                'CS701 - Artificial Intelligence',
                'CS801 - Computer Networks',
            ],
            'Statistics': [
                'STAT101 - Introduction to Statistics',
                'STAT201 - Probability Theory',
                'STAT301 - Statistical Inference',
                'STAT401 - Regression Analysis',
                'STAT501 - Time Series Analysis',
                'STAT601 - Multivariate Statistics',
                'STAT701 - Bayesian Statistics',
            ],
            'Data Science': [
                'DS101 - Introduction to Data Science',
                'DS201 - Data Visualization',
                'DS301 - Statistical Computing',
                'DS401 - Big Data Analytics',
                'DS501 - Data Mining',
                'DS601 - Deep Learning',
                'DS701 - Natural Language Processing',
            ],
            'Physics': [
                'PHY101 - General Physics I',
                'PHY201 - General Physics II',
                'PHY301 - Mechanics',
                'PHY401 - Electromagnetism',
                'PHY501 - Quantum Mechanics',
                'PHY601 - Thermodynamics',
                'PHY701 - Astrophysics',
            ],
            'Chemistry': [
                'CHEM101 - General Chemistry I',
                'CHEM201 - General Chemistry II',
                'CHEM301 - Organic Chemistry',
                'CHEM401 - Physical Chemistry',
                'CHEM501 - Biochemistry',
                'CHEM601 - Analytical Chemistry',
                'CHEM701 - Inorganic Chemistry',
            ],
            'Mathematics': [
                'MATH101 - Calculus I',
                'MATH201 - Calculus II',
                'MATH301 - Linear Algebra',
                'MATH401 - Differential Equations',
                'MATH501 - Real Analysis',
                'MATH601 - Abstract Algebra',
                'MATH701 - Topology',
            ],
            'Biology': [
                'BIO101 - General Biology I',
                'BIO201 - General Biology II',
                'BIO301 - Cell Biology',
                'BIO401 - Genetics',
                'BIO501 - Ecology',
                'BIO601 - Evolution',
                'BIO701 - Molecular Biology',
            ]
        }

        updated_count = 0
        created_count = 0

        for department, subjects in department_subjects.items():
            for subject_name in subjects:
                # Extract the subject code and name
                if ' - ' in subject_name:
                    code, name = subject_name.split(' - ', 1)
                else:
                    code = subject_name
                    name = subject_name

                # Try to find existing subject by name
                subject, created = SubjectTag.objects.get_or_create(
                    name=name,
                    defaults={
                        'slug': code.lower().replace(' ', '-'),
                        'department': department,
                        'education_level': 'bachelors'  # Default to bachelors
                    }
                )

                if created:
                    created_count += 1
                    self.stdout.write(f"Created: {subject.name} in {department}")
                else:
                    # Update existing subject with department
                    if subject.department != department:
                        subject.department = department
                        subject.save()
                        updated_count += 1
                        self.stdout.write(f"Updated: {subject.name} with department {department}")

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully processed subjects. Created: {created_count}, Updated: {updated_count}'
            )
        )
