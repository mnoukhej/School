from django.urls import path
from . import views

app_name = 'school_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('academics/', views.academics, name='academics'),
    path('streams/', views.streams, name='streams'),
    path('stream/<str:name>/', views.stream_detail, name='stream_detail'),
    path('notices-and-events/', views.notices_and_events, name='notices_and_events'),
    path('notices/', views.notices, name='notices'),
    path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('events/', views.events, name='events'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('faculty/', views.faculty_list, name='faculty_list'),
    path('faculty/<slug:slug>/', views.faculty_detail, name='faculty_detail'),
    path('admission/', views.admission, name='admission'),
    path('contact/', views.contact, name='contact'),
    path('submit-inquiry/', views.submit_inquiry, name='submit_inquiry'),
    path('girls-hostel/', views.girls_hostel, name='girls_hostel'),
]
