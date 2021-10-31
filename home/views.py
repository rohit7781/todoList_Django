from django.shortcuts import render,HttpResponse
from home.models import todos
# Create your views here.
def task(request):
    alltask = todos.objects.all()
    context = {'task':alltask}

    return render(request,'task.html',context)
def index(request):
    context = {'success':False}
    if request.method=='POST':
        titles = request.POST['title']
        desc = request.POST['desc']
        ins = todos(title= titles,desc=desc)
        ins.save()
        context = {'success':True}
        # print(titles,desc)

    return render(request,'index.html',context)
