from django.shortcuts import render_to_response

# Create your views here.
def timetable(request):
	return render_to_response('timetable.html')

def faculty(request):
	return render_to_response('faculty.html')

def developers(request):
	return render_to_response('developers.html')

def sem2(request):
	return render_to_response('sem2.html')

def sem4(request):
	return render_to_response('sem4.html')


def sem6(request):
	return render_to_response('sem6.html')


def sem8(request):
	return render_to_response('sem8.html')
