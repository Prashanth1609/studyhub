from django.core.management.base import BaseCommand
from core.models import SubjectTag

class Command(BaseCommand):
    help = 'Create subjects for different education levels'

    def handle(self, *args, **options):
        # Bachelors level subjects
        bachelors_subjects = [
            'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Computer Science',
            'Engineering', 'Business Administration', 'Economics', 'Psychology',
            'Sociology', 'History', 'Literature', 'Philosophy', 'Art History',
            'Political Science', 'Geography', 'Environmental Science', 'Statistics',
            'Accounting', 'Marketing', 'Finance', 'Human Resources', 'Operations Management',
            'Information Technology', 'Data Science', 'Web Development', 'Mobile Development',
            'Database Management', 'Network Security', 'Software Engineering', 'Digital Marketing'
        ]

        # Masters level subjects
        masters_subjects = [
            'Advanced Mathematics', 'Quantum Physics', 'Advanced Chemistry', 'Molecular Biology',
            'Advanced Computer Science', 'Advanced Engineering', 'MBA', 'Advanced Economics',
            'Clinical Psychology', 'Advanced Sociology', 'Advanced History', 'Advanced Literature',
            'Advanced Philosophy', 'Advanced Political Science', 'Environmental Policy',
            'Advanced Statistics', 'Financial Analysis', 'Strategic Management', 'Business Analytics',
            'Advanced Information Technology', 'Machine Learning', 'Artificial Intelligence',
            'Advanced Data Science', 'Cloud Computing', 'Cybersecurity', 'Advanced Software Engineering',
            'Project Management', 'Leadership', 'Innovation Management', 'International Business'
        ]

        # PhD level subjects
        phd_subjects = [
            'Research Methodology', 'Advanced Research Design', 'Statistical Analysis',
            'Theoretical Physics', 'Advanced Quantum Mechanics', 'Advanced Organic Chemistry',
            'Advanced Molecular Biology', 'Advanced Algorithms', 'Advanced Systems Engineering',
            'Advanced Business Research', 'Advanced Economic Theory', 'Advanced Psychological Research',
            'Advanced Sociological Theory', 'Advanced Historical Research', 'Advanced Literary Theory',
            'Advanced Philosophical Research', 'Advanced Political Theory', 'Environmental Research',
            'Advanced Statistical Research', 'Advanced Financial Research', 'Advanced Management Research',
            'Advanced Technology Research', 'Advanced AI Research', 'Advanced Data Research',
            'Advanced Software Research', 'Advanced Security Research', 'Advanced Engineering Research',
            'Advanced Business Research', 'Advanced Social Research', 'Advanced Humanities Research'
        ]

        # Create subjects for each education level
        education_levels = [
            (SubjectTag.BACHELORS, bachelors_subjects),
            (SubjectTag.MASTERS, masters_subjects),
            (SubjectTag.PHD, phd_subjects)
        ]

        created_count = 0
        for education_level, subjects in education_levels:
            for subject_name in subjects:
                # Create slug from name
                slug = subject_name.lower().replace(' ', '-').replace('&', 'and')
                
                # Check if subject already exists for this education level
                subject, created = SubjectTag.objects.get_or_create(
                    name=subject_name,
                    education_level=education_level,
                    defaults={'slug': slug}
                )
                
                if created:
                    created_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(f'Created: {subject_name} ({education_level})')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Already exists: {subject_name} ({education_level})')
                    )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} new subjects')
        )
