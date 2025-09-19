from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import SubjectTag, UserProfile

class Command(BaseCommand):
    help = 'Check the current state of subjects and user profiles'

    def handle(self, *args, **options):
        self.stdout.write("=== DATABASE STATUS CHECK ===")
        
        # Check subjects
        self.stdout.write("\n--- SUBJECTS ---")
        total_subjects = SubjectTag.objects.count()
        self.stdout.write(f"Total subjects: {total_subjects}")
        
        if total_subjects > 0:
            # Show subjects by education level
            for level in ['bachelors', 'masters', 'phd']:
                count = SubjectTag.objects.filter(education_level=level).count()
                self.stdout.write(f"  {level.title()}: {count}")
            
            # Show subjects by department
            self.stdout.write("\n--- SUBJECTS BY DEPARTMENT ---")
            departments = SubjectTag.objects.values_list('department', flat=True).distinct()
            for dept in departments:
                if dept:
                    count = SubjectTag.objects.filter(department=dept).count()
                    self.stdout.write(f"  {dept}: {count}")
                else:
                    count = SubjectTag.objects.filter(department__isnull=True).count()
                    self.stdout.write(f"  No Department: {count}")
        
        # Check user profiles
        self.stdout.write("\n--- USER PROFILES ---")
        total_users = User.objects.count()
        total_profiles = UserProfile.objects.count()
        self.stdout.write(f"Total users: {total_users}")
        self.stdout.write(f"Total profiles: {total_profiles}")
        
        if total_profiles > 0:
            # Show education level distribution
            for level in ['bachelors', 'masters', 'phd']:
                count = UserProfile.objects.filter(education_level=level).count()
                self.stdout.write(f"  {level.title()}: {count}")
        
        # Check for users without profiles
        users_without_profiles = User.objects.filter(profile__isnull=True).count()
        if users_without_profiles > 0:
            self.stdout.write(f"\n⚠️  Users without profiles: {users_without_profiles}")
        
        # Check for subjects without departments
        subjects_without_dept = SubjectTag.objects.filter(department__isnull=True).count()
        if subjects_without_dept > 0:
            self.stdout.write(f"⚠️  Subjects without departments: {subjects_without_dept}")
        
        self.stdout.write("\n=== END CHECK ===")
