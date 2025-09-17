# core/admin.py
from django.contrib import admin
from .models import StudySession, SessionMember, Message, SubjectTag, UserProfile


class SessionMemberInline(admin.TabularInline):
    model = SessionMember
    extra = 0


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0


@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'start_time', 'end_time', 'is_virtual', 'capacity')
    list_filter = ('is_virtual', 'start_time')
    search_fields = ('title', 'description', 'owner__username')
    inlines = [SessionMemberInline, MessageInline]


@admin.register(SubjectTag)
class SubjectTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'education_level', 'department')
    list_filter = ('education_level', 'department')
    search_fields = ('name', 'slug')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'education_level', 'is_student_leader', 'created_at')
    list_filter = ('education_level', 'is_student_leader', 'created_at')
    search_fields = ('user__username', 'user__email')
