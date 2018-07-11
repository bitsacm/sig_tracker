from . models import Sig
from . models import Topics
from django.shortcuts import render
from django.http import Http404


def index(request):
    all_sig = Sig.objects.all()
    #context = {'all_sig': all_sig }
    return render(request,'about_sig/index.html',{'all_sig': all_sig})

def detail(request, sig_id):
    try:
        sig = Sig.objects.get(pk=sig_id)
    except Sig.DoesNotExist:
        raise Http404("SIG does not exist")
    return render(request, 'about_sig/detail.html', {'sig': sig})
