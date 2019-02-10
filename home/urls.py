from django.urls import path
from . import views

urlpatterns = [
    path('timetable/', views.timetable, name='timetable'),
    path('faculty/', views.faculty, name='faculty'),
    path('developers/', views.developers, name='developers'),
]
