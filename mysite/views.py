from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo


# Create your views here.
def HomeView(request):
    todo_queryset = Todo.objects.all()
    content = {"todo": todo_queryset}
    return render(request, "index.html", context=content)


def FormView(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        status = request.POST.get("status")
        Todo.objects.create(title=title, description=description, status=status)
        return redirect(HomeView)
    content = {"method": "post"}
    return render(request, "form.html", context=content)


def edit_todo(request, pk):
    queryset = Todo.objects.get(id=pk)
    if request.method == "POST":
        queryset.title = request.POST.get("title")
        queryset.description = request.POST.get("description")
        queryset.status = request.POST.get("status")
        queryset.save()
        return redirect("home")
    content = {"object": queryset, "method": "edit"}
    return render(request, "form.html", context=content)


def delete(request, pk):
    queryset = Todo.objects.get(id=pk)
    queryset.delete()
    return redirect(HomeView)
