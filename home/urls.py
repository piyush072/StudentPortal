from django.urls import path
from . import views

urlpatterns = [
    path('timetable/', views.timetable, name='timetable'),
    path('faculty/', views.faculty, name='faculty'),
    path('developers/', views.developers, name='developers'),
    path('timetable/sem2', views.sem2, name='sem2'),
    path('timetable/sem4', views.sem4, name='sem4'),
    path('timetable/sem6', views.sem6, name='sem6'),
    path('timetable/sem8', views.sem8, name='sem8'),
]
