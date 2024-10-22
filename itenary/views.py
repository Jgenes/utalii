from django.shortcuts import render

# Create your views here.

def itenary_list(request):
	return render(request, "dashboard/iternary_list.html");
