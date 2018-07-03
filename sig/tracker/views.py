from django.shortcuts import render

from django.http import HttpResponse

from .models import SIG


"""Home page for sig_tracker website
"""
def home(request):
    return render(request, 'tracker/home.html')


"""This shows the list of current SIGs
"""
def sig(request):
    sig_list = SIG.objects.all()
    context = {'sig_list': sig_list}
    return render(request, 'tracker/sig.html', context)


"""This is for information about each individual SIG
"""
def sig_details(request, sig_id):
    sig = SIG.objects.get(pk=sig_id)
    context = {'sig': sig}
    return render(request, 'tracker/details.html', context)
