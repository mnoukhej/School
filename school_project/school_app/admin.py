from django.contrib import admin
from .models import Inquiry, Notice, Event, Faculty, About, Stream

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'department', 'experience', 'is_active')
    list_filter = ('department', 'is_active', 'joining_date')
    search_fields = ('name', 'designation', 'department', 'qualification')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active',)
    date_hierarchy = 'joining_date'

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated')
    search_fields = ('title', 'content')

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description', 'subjects')
    list_editable = ('is_active',)

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'parent_name', 'contact_number', 'admission_class', 'preferred_medium', 'created_at')
    list_filter = ('admission_class', 'preferred_medium', 'created_at')
    search_fields = ('student_name', 'parent_name', 'contact_number')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_posted', 'is_active')
    list_filter = ('is_active', 'category', 'date_posted')
    search_fields = ('title', 'content')
    date_hierarchy = 'date_posted'
    ordering = ('-date_posted',)
    list_editable = ('is_active',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'venue', 'registration_required', 'is_active')
    list_filter = ('is_active', 'registration_required', 'date')
    search_fields = ('title', 'description', 'venue')
    date_hierarchy = 'date'
    ordering = ('-date',)
    list_editable = ('is_active', 'registration_required')
