from django.shortcuts import render,redirect
import django
from django.views.generic import View


from rest_framework import generics

from django.http import Http404,QueryDict

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.contrib.auth.models import User
from serializers import *
from models import *
from forms import *
# Create your views here.
def index(request):
    template="restApp/index.html"
    context={}

    if request.method=="POST":
        form=instanceIDForm(request.POST)

        if form.is_valid():
            data=form.cleaned_data
            instance=data["instanceID"]
            name=data["name"]

            inst=Instance.objects.get(instanceID=instance)
            person=Person(name=name,instance=inst,score=0)
            person.save()
            response= redirect("inInstance")
            response.set_cookie("username",name)
            return response

    else:
        form=instanceIDForm()
        name=None
    context["form"]=form
    response=render(request,template,context)
    if name:
        response.set_cookie("username",name)
    return response

def inInstance(request):
    template="restApp/inInstance.html"
    context={}
    if "username" in request.COOKIES:
        username=request.COOKIES["username"]
        context["username"]=username
    else:
        context["username"]=request.COOKIES
    return render(request,template,context)


class instanceDetail(APIView):

    def get_object(self,instanceID):
        try:
            return Instance.objects.get(instanceID=instanceID)
        except Instance.DoesNotExist:
            raise Http404

    def get(self,request,instanceID):
        instance=self.get_object(instanceID)
        serializer=instanceSerializer(instance)
        return Response(serializer.data)

    def put(self,request,instanceID):
        instance=self.get_object(instanceID)
        serializer=instanceSerializer(instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,instanceID):
        instance=self.get_object(instanceID)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class peopleByInstance(APIView):
    def get_people(self,instanceID):
        try:
            instance=Instance.objects.get(instanceID=instanceID)
            people=Person.objects.filter(instance=instance)
            return people
        except:
            raise Http404
    def get(self,request,instanceID):
        people=self.get_people(instanceID)
        serializer=personSerializer(people,many=True)
        return Response(serializer.data)
class ScoreUpdate(APIView):

    def put(self,request,personPk):
        person=Person.objects.get(pk=personPk)
        data=request.query_params
        points=data["points"]
        add=data["add"]
        print points,
        print add
        if add:
            person.score=person.score+int(points)
        else:
            person.score=person.score-int(points)
        person.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def get(self,request,personPk):
        person=Person.objects.get(pk=personPk)
        return Response(person.score)
