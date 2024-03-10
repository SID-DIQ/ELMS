from django.shortcuts import render

def BASE(request):
    return render(request, 'base.html')

def HOME(request):
    return render(request, 'Main/home.html')

def SINGLE_COURSE(request):
    return render(request, 'Main/single_course.html')

def ABOUTUS(request):
    return render(request, 'Main/aboutus.html')