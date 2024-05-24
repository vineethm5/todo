from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages


def home(req):
    itemlist=todo.objects.order_by("-date")
    if req.method == 'POST':
        form=todoform(req.POST)
        if form.is_valid:
            form.save()
            messages.info(req,"Note Added Successfully")
            return redirect("/")
        else:
            form=todoform()
    form=todoform()
    page={
        'title':"Title",
        'forms':form,
        'list':itemlist
    }
    return render(req,"home.html",page)


def dele(req,id):
    if req.method == "POST":
        queryset=todo.objects.get(id=id)
        queryset.delete()
        messages.info(req,"Notes deleted Successfully")
        return redirect("/")





# Create your views here.
#https://www.geeksforgeeks.org/python-todo-webapp-using-django/?ref=lbp
