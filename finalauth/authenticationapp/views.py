from django.shortcuts import render,HttpResponse, redirect

def home(request):
    return HttpResponse('Caleb Mayaka')
