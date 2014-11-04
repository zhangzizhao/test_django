#model admin form
from django.shortcuts import render, render_to_response, RequestContext
from .forms import peopleForm
#rest_form
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tt.serializers import UserSerializer, GroupSerializer

#~~  begin
def home(request):
    form = peopleForm(request.POST or None)            #form model
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    return render_to_response("zz.html",
                              locals(),
                              context_instance=RequestContext(request))

#~~~~~~~~~~~~~~~~
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
