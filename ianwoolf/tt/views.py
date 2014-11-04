from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.
from .forms import peopleForm

def home(request):
    print 'begin'
    form = peopleForm(request.POST or None)
    print 'BEFORE IF'
    if form.is_valid():
        print 'if in'
        save_it = form.save(commit=False)
        save_it.save()
    print 'out'
    return render_to_response("zz.html",
                              locals(),
                              context_instance=RequestContext(request))


