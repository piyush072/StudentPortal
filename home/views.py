from django.shortcuts import render_to_response

# Create your views here.
def timetable(request):
	return render_to_response('timetable.html')

def faculty(request):
	return render_to_response('faculty.html')

def developers(request):
	return render_to_response('developers.html')
