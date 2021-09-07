from django.shortcuts import render
from django.utils.html import format_html
from crud import forms
from crud.models import Userprofile
# Create your views here.

def home(request):
    userlist = Userprofile.objects.order_by('phone')
    diction = {'title':"Home", 'users': userlist}
    return render(request, 'crud/index.html', context=diction)

def user(request):
    form = forms.Users()

    if request.method == "POST":
      form = forms.Users(request.POST)
      
      if form.is_valid():
          form.save(commit=True)
          return home(request)

    diction = {'title':"User Form", "userform": form}
    return render(request, 'crud/userform.html', context=diction)


def userform(request):
    form = forms.Userform()

    if request.method == "POST":
      form = forms.Userform(request.POST)
      
      if form.is_valid():
          form.save(commit=True)
          return home(request)

    diction = {'title':"User Form", "userform": form}
    return render(request, 'crud/userform.html', context=diction)


def userprofile(request,userid):
    userinfo = Userprofile.objects.get(pk=userid)
    diction = {'title':"Userprofile", 'userinfo': userinfo}
    return render(request, 'crud/userprofile.html', context=diction)


def userupdate(request,userid):
    userinfo = Userprofile.objects.get(pk=userid)
    form = forms.Userform(instance= userinfo)

    if request.method == "POST":
         form = forms.Userform(request.POST, instance=userinfo)

         if form.is_valid():
             form.save(commit=True)
             return home(request)

    diction = {'title':"Update", 'userinfo': form}
    return render(request, 'crud/userupdate.html', context=diction)



def userdelete(request,userid):
    userinfo = Userprofile.objects.get(pk=userid).delete()
    diction = {'title':"Userdelete", 'delete_mss': "Delete Done"}
    return render(request, 'crud/userdelete.html', context=diction)

