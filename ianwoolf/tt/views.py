#model admin form
from django.shortcuts import render, render_to_response, RequestContext
from .forms import peopleForm
#rest_form
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tt.serializers import UserSerializer, GroupSerializer
#rest_ser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from tt.models import people
from tt.serializers import peopleSerializer
#~~  begin
#tu 2 api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
#tu3 base view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
#~
from rest_framework import mixins
from rest_framework import generics

#from rest_framework.response import Response

def home(request):
    form = peopleForm(request.POST or None)            #form model
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    return render_to_response("zz.html",
                              locals(),
                              context_instance=RequestContext(request))

#~~~~~~~~~~~~~~~~~~~~~~~
#tu2 api_view begin

#class JSONResponse(HttpResponse):
#    """
#    An HttpResponse that renders its content into JSON.
#    """
#    def __init__(self, data, **kwargs):
#        content = JSONRenderer().render(data)
#        kwargs['content_type'] = 'application/json'
#        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET','POST'])
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = people.objects.all()
        serializer = peopleSerializer(snippets, many=True)
        #serializer = peopleSerializer(people)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = peopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return Response(serializer.errors, status=400)
@api_view(['GET','PUT','DELETE'])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = people.objects.get(pk=pk)
    except people.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = peopleSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = peopleSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=204)
# ser end     
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# tu3 base view begin
class PeopleList(APIView):
    def get(self, request, format=None):
        this_people = people.objects.all()
        print this_people
        serializer = peopleSerializer(this_people, many=True)
        print "done",serializer.data
        print serializer.data
        print "done"
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = peopleSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PeopleDetail(APIView):
    def get_object(self, pk):
        try:
            return people.objects.get(pk=pk)
        except people.DoseNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        this_people = self.get_object(pk)
        serializer = peopleSerializer(this_people)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        this_people = self.get_object(pk)
        serializer = peopleSerializer(this_people, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        this_people = self.get_object(pk)
        this_people.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#~
class PeopleList2(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = people.objects.all()
    serializer_class = peopleSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
class PeopleDetail2(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,  generics.GenericAPIView):
    queryset = people.objects.all()
    serializer_class = peopleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
#~
class PeopleList3(generics.ListCreateAPIView):
    queryset = people.objects.all()
    serializer_class = peopleSerializer


class PeopleDetail3(generics.RetrieveUpdateDestroyAPIView):
    queryset = people.objects.all()
    serializer_class = peopleSerializer
## tu3 end  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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

def myown(request):
#    form = peopleForm(request.POST or None)            #form model
#    if form.is_valid():
#        save_it = form.save(commit=False)
#        save_it.save()
    return render_to_response("test.html",
                             )
