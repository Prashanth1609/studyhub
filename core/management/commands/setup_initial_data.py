from django.core.management.base import BaseCommand
from core.models import SubjectTag

class Command(BaseCommand):
    help = 'Set up initial data for the application'

    def handle(self, *args, **options):
        # Create basic subjects if they don't exist
        subjects_data = [
            # Computer Science
            {'name': 'Programming Fundamentals', 'department': 'Computer Science', 'education_level': 'Undergraduate'},
            {'name': 'Data Structures', 'department': 'Computer Science', 'education_level': 'Undergraduate'},
            {'name': 'Algorithms', 'department': 'Computer Science', 'education_level': 'Undergraduate'},
            {'name': 'Database Systems', 'department': 'Computer Science', 'education_level': 'Undergraduate'},
            {'name': 'Software Engineering', 'department': 'Computer Science', 'education_level': 'Undergraduate'},
            
            # Mathematics
            {'name': 'Calculus I', 'department': 'Mathematics', 'education_level': 'Undergraduate'},
            {'name': 'Calculus II', 'department': 'Mathematics', 'education_level': 'Undergraduate'},
            {'name': 'Linear Algebra', 'department': 'Mathematics', 'education_level': 'Undergraduate'},
            {'name': 'Statistics', 'department': 'Mathematics', 'education_level': 'Undergraduate'},
            
            # Physics
            {'name': 'Physics I', 'department': 'Physics', 'education_level': 'Undergraduate'},
            {'name': 'Physics II', 'department': 'Physics', 'education_level': 'Undergraduate'},
            {'name': 'Mechanics', 'department': 'Physics', 'education_level': 'Undergraduate'},
            
            # Other
            {'name': 'Other', 'department': 'Other', 'education_level': 'All'},
        ]
        
        created_count = 0
        for subject_data in subjects_data:
            subject, created = SubjectTag.objects.get_or_create(
                name=subject_data['name'],
                defaults={
                    'department': subject_data['department'],
                    'education_level': subject_data['education_level']
                }
            )
            if created:
                created_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} new subjects')
        )
