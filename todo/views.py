from . models import TodoModels
from django.shortcuts import render, redirect
from .forms import TodoForms
from django.views.decorators.http import require_POST
# Create your views here.


def IndexView(request):
    model = TodoModels.objects.order_by('id')
    form = TodoForms
    context = {"model": model, "form": form}
    return render(request, 'index.html', context)


'''@require_POST
def AddNewTodo(request):
    form = TodoForms(request.POST)
    if form.is_valid():
        my_new_todo = TodoModels(task=request.POST['text'])
        my_new_todo.save()
        return redirect('index')
    return redirect('index')'''


def AddNewTodo(request):
    form = TodoForms(request.POST)
    if form.is_valid():
        myForm = TodoModels(task=request.POST['text'])
        myForm.save()
        print(myForm)
        #return render(request, 'chutiya.html')
        return redirect('index')
    else:
        return render(request, 'bhlu.html')


def MarkCompleteTodo(request, todo_id):
    model = TodoModels.objects.get(pk=todo_id)
    model.complete = True
    model.save()
    return redirect('index')


def MarkIncompleteTodo(request, todo_id):
    model = TodoModels.objects.get(pk=todo_id)
    model.complete = False
    model.save()
    return redirect('index')


def DeleteTodo(request):
    TodoModels.objects.filter(complete__exact=True).delete()
    return redirect('index')
