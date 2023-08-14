from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Todo
import json

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, 'base.html', {"todo_list": todos})


@require_http_methods(["POST"])
def add(request):
    body = request.body.decode("utf-8")
    body = json.loads(body)
    title = body.get("title", "")
    todo = Todo(title=title)
    todo.save()
    return JsonResponse({"todo_id": todo.id, "complete": todo.complete, "todo_title": todo.title})


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return JsonResponse({"todo_id": todo_id, "complete": todo.complete})


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return JsonResponse({"todo_id": todo_id})
