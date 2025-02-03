from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Notice, Event, Faculty, About, Stream, Inquiry
from .forms import InquiryForm

def home(request):
    notices = Notice.objects.filter(is_active=True)[:3]
    upcoming_events = Event.objects.filter(is_active=True)[:3]
    faculty_members = Faculty.objects.filter(is_active=True)[:4]
    streams = Stream.objects.filter(is_active=True)
    
    context = {
        'notices': notices,
        'upcoming_events': upcoming_events,
        'faculty_members': faculty_members,
        'streams': streams,
    }
    return render(request, 'school_app/index.html', context)

def about(request):
    about_content = About.objects.first()
    faculty_count = Faculty.objects.filter(is_active=True).count()
    context = {
        'about': about_content,
        'faculty_count': faculty_count,
    }
    return render(request, 'school_app/about.html', context)

def academics(request):
    streams = Stream.objects.filter(is_active=True)
    context = {
        'streams': streams,
    }
    return render(request, 'school_app/academics.html', context)

def streams(request):
    streams = Stream.objects.filter(is_active=True)
    context = {
        'streams': streams,
    }
    return render(request, 'school_app/streams.html', context)

def stream_detail(request, name):
    stream = get_object_or_404(Stream, name=name, is_active=True)
    context = {
        'stream': stream,
    }
    return render(request, 'school_app/stream_detail.html', context)

def notices(request):
    notices = Notice.objects.all().order_by('-date')
    return render(request, 'school_app/notices.html', {
        'notices': notices
    })

def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk, is_active=True)
    context = {
        'notice': notice,
    }
    return render(request, 'school_app/notice_detail.html', context)

def events(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'school_app/events.html', {
        'events': events
    })

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk, is_active=True)
    context = {
        'event': event,
    }
    return render(request, 'school_app/event_detail.html', context)

def faculty_list(request):
    departments = Faculty.objects.filter(is_active=True).values_list('department', flat=True).distinct()
    faculty_by_dept = {}
    
    for dept in departments:
        faculty_by_dept[dept] = Faculty.objects.filter(department=dept, is_active=True)
    
    context = {
        'faculty_by_dept': faculty_by_dept,
    }
    return render(request, 'school_app/faculty_list.html', context)

def faculty_detail(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug, is_active=True)
    context = {
        'faculty': faculty,
    }
    return render(request, 'school_app/faculty_detail.html', context)

def admission(request):
    form = InquiryForm()
    context = {
        'form': form,
    }
    return render(request, 'school_app/admission.html', context)

def contact(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('school_app:contact')
    else:
        form = InquiryForm()
    
    context = {
        'form': form,
    }
    return render(request, 'school_app/contact.html', context)

def submit_inquiry(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your inquiry has been submitted successfully!')
            return redirect('school_app:home')
    else:
        form = InquiryForm()
    
    context = {
        'form': form,
    }
    return render(request, 'school_app/inquiry_form.html', context)

def notices_and_events(request):
    notices = Notice.objects.all().order_by('-date_posted')
    events = Event.objects.all().order_by('date')
    return render(request, 'school_app/notices_and_events.html', {
        'notices': notices,
        'events': events
    })

def girls_hostel(request):
    return render(request, 'school_app/girls_hostel.html')

def handler404(request, exception):
    return render(request, 'school_app/404.html', status=404)

def handler500(request):
    return render(request, 'school_app/500.html', status=500)
