from django.db import models
from django.utils.text import slugify

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    experience = models.PositiveIntegerField(help_text="Experience in years")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    photo = models.ImageField(upload_to='faculty/', blank=True)
    bio = models.TextField()
    joining_date = models.DateField()
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Faculty Members"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.designation}"

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Stream(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    subjects = models.TextField(help_text="Enter subjects separated by commas")
    image = models.ImageField(upload_to='streams/', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Inquiry(models.Model):
    MEDIUM_CHOICES = [
        ('Bengali', 'Bengali'),
        ('Urdu', 'Urdu'),
    ]
    CLASS_CHOICES = [(str(i), f'Class {i}') for i in range(5, 13)]
    
    student_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    admission_class = models.CharField(max_length=2, choices=CLASS_CHOICES)
    preferred_medium = models.CharField(max_length=10, choices=MEDIUM_CHOICES)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Inquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student_name} - Class {self.admission_class}"

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    attachment = models.FileField(upload_to='notices/', blank=True)
    category = models.CharField(max_length=50, choices=[
        ('general', 'General'),
        ('academic', 'Academic'),
        ('exam', 'Examination'),
        ('event', 'Event'),
    ], default='general')

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/', blank=True)
    is_active = models.BooleanField(default=True)
    registration_required = models.BooleanField(default=False)
    max_participants = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
