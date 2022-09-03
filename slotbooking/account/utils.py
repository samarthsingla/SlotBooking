from django.shortcuts import render, HttpResponse
def error1(request, msg):
    return render(request, "account/genericError.html", {"error_message":msg})