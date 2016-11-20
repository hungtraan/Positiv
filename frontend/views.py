from django.shortcuts import render

def home(request):
	d = {}
	d['title'] = 'Home'
	d['exit_button'] = False
	d['name'] = 'Hung'

	return render(request, 'home-positiv.html', d)

def diary(request):
	d = {}
	d['title'] = 'Diary'
	d['exit_button'] = False
	return render(request, 'entries.html', d)
	
def graphs(request):
	d = {}
	d['title'] = 'Graphs'
	d['exit_button'] = False
	return render(request, 'graphs.html', d)
	
def profile(request):
	d = {}
	d['title'] = 'Profile'
	d['exit_button'] = False
	return render(request, 'profile.html', d)

def reflection1(request):
	d = {}
	d['title'] = 'Reflection 1'
	d['returning_addr'] = '/'
	d['exit_button'] = True
	return render(request, 'reflection-1.html', d)

def reflection2(request):
	d = {}
	d['title'] = 'Reflection 1'
	d['returning_addr'] = '/'
	d['exit_button'] = True
	return render(request, 'reflection-2.html', d)

def reflection3(request):
	d = {}
	d['title'] = 'Reflection 1'
	d['returning_addr'] = '/'
	d['exit_button'] = True
	return render(request, 'reflection-3.html', d)

def reflection4(request):
	d = {}
	d['title'] = 'Reflection 1'
	d['returning_addr'] = '/'
	d['exit_button'] = True
	return render(request, 'reflection-4.html', d)