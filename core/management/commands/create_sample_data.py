from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from core.models import SubjectTag, StudySession, SessionMember, Message

class Command(BaseCommand):
    help = 'Create sample data for StudyHub'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create sample users
        user1, created = User.objects.get_or_create(
            username='john_doe',
            defaults={
                'email': 'john@example.com',
                'first_name': 'John',
                'last_name': 'Doe'
            }
        )
        if created:
            user1.set_password('password123')
            user1.save()
            self.stdout.write(f'Created user: {user1.username}')
        
        user2, created = User.objects.get_or_create(
            username='jane_smith',
            defaults={
                'email': 'jane@example.com',
                'first_name': 'Jane',
                'last_name': 'Smith'
            }
        )
        if created:
            user2.set_password('password123')
            user2.save()
            self.stdout.write(f'Created user: {user2.username}')
        
        user3, created = User.objects.get_or_create(
            username='mike_wilson',
            defaults={
                'email': 'mike@example.com',
                'first_name': 'Mike',
                'last_name': 'Wilson'
            }
        )
        if created:
            user3.set_password('password123')
            user3.save()
            self.stdout.write(f'Created user: {user3.username}')
        
        # Create subject tags
        subjects_data = [
            {'name': 'Mathematics', 'slug': 'mathematics'},
            {'name': 'Physics', 'slug': 'physics'},
            {'name': 'Computer Science', 'slug': 'computer-science'},
            {'name': 'Biology', 'slug': 'biology'},
            {'name': 'Chemistry', 'slug': 'chemistry'},
            {'name': 'Literature', 'slug': 'literature'},
            {'name': 'History', 'slug': 'history'},
            {'name': 'Economics', 'slug': 'economics'},
        ]
        
        subjects = {}
        for subject_data in subjects_data:
            subject, created = SubjectTag.objects.get_or_create(
                slug=subject_data['slug'],
                defaults={'name': subject_data['name']}
            )
            subjects[subject.slug] = subject
            if created:
                self.stdout.write(f'Created subject: {subject.name}')
        
        # Create sample study sessions
        now = timezone.now()
        
        # Session 1: Virtual Math Study Group
        session1, created = StudySession.objects.get_or_create(
            title='Advanced Calculus Study Group',
            defaults={
                'owner': user1,
                'description': 'Weekly study session for advanced calculus topics. We\'ll cover integration techniques, series, and applications.',
                'start_time': now + timedelta(days=1, hours=14),
                'end_time': now + timedelta(days=1, hours=16),
                'is_virtual': True,
                'virtual_link': 'https://meet.google.com/abc-defg-hij',
                'capacity': 10
            }
        )
        if created:
            session1.subjects.add(subjects['mathematics'])
            SessionMember.objects.create(session=session1, user=user1, role=SessionMember.HOST)
            SessionMember.objects.create(session=session1, user=user2)
            SessionMember.objects.create(session=session1, user=user3)
            self.stdout.write(f'Created session: {session1.title}')
        
        # Session 2: In-person Physics Lab
        session2, created = StudySession.objects.get_or_create(
            title='Physics Lab Review',
            defaults={
                'owner': user2,
                'description': 'Review session for upcoming physics lab exam. We\'ll go through key experiments and calculations.',
                'start_time': now + timedelta(days=2, hours=10),
                'end_time': now + timedelta(days=2, hours=12),
                'is_virtual': False,
                'location_text': 'Science Building, Room 205',
                'capacity': 8
            }
        )
        if created:
            session2.subjects.add(subjects['physics'])
            SessionMember.objects.create(session=session2, user=user2, role=SessionMember.HOST)
            SessionMember.objects.create(session=session2, user=user1)
            self.stdout.write(f'Created session: {session2.title}')
        
        # Session 3: Computer Science Project
        session3, created = StudySession.objects.get_or_create(
            title='Web Development Project',
            defaults={
                'owner': user3,
                'description': 'Collaborative web development project. We\'ll work on building a full-stack application using Django and React.',
                'start_time': now + timedelta(days=3, hours=15),
                'end_time': now + timedelta(days=3, hours=18),
                'is_virtual': True,
                'virtual_link': 'https://zoom.us/j/123456789',
                'capacity': 6
            }
        )
        if created:
            session3.subjects.add(subjects['computer-science'])
            SessionMember.objects.create(session=session3, user=user3, role=SessionMember.HOST)
            SessionMember.objects.create(session=session3, user=user1)
            SessionMember.objects.create(session=session3, user=user2)
            self.stdout.write(f'Created session: {session3.title}')
        
        # Session 4: Biology Study Group
        session4, created = StudySession.objects.get_or_create(
            title='Cell Biology Review',
            defaults={
                'owner': user1,
                'description': 'Comprehensive review of cell biology concepts for the midterm exam.',
                'start_time': now + timedelta(days=4, hours=13),
                'end_time': now + timedelta(days=4, hours=15),
                'is_virtual': False,
                'location_text': 'Biology Department, Conference Room A',
                'capacity': 12
            }
        )
        if created:
            session4.subjects.add(subjects['biology'])
            SessionMember.objects.create(session=session4, user=user1, role=SessionMember.HOST)
            self.stdout.write(f'Created session: {session4.title}')
        
        # Add some sample messages
        messages_data = [
            (session1, user2, 'Looking forward to the calculus session!'),
            (session1, user3, 'Should I bring my textbook?'),
            (session1, user1, 'Yes, please bring your textbook and calculator.'),
            (session2, user1, 'What experiments will we be reviewing?'),
            (session2, user2, 'We\'ll cover mechanics, electricity, and optics.'),
            (session3, user1, 'What tech stack are we using?'),
            (session3, user3, 'Django for backend, React for frontend, and PostgreSQL for database.'),
        ]
        
        for session, user, text in messages_data:
            message, created = Message.objects.get_or_create(
                session=session,
                user=user,
                text=text,
                defaults={'created_at': now - timedelta(hours=2)}
            )
            if created:
                self.stdout.write(f'Created message from {user.username}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )
        self.stdout.write('Sample users created:')
        self.stdout.write('- john_doe (password: password123)')
        self.stdout.write('- jane_smith (password: password123)')
        self.stdout.write('- mike_wilson (password: password123)')
        self.stdout.write('- admin (superuser)')
