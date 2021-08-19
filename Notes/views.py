from django.shortcuts import render,HttpResponse,redirect
from .models import Document
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import DocumentForm
from django.contrib import messages
# Create your views here.

def index(request):

   documents = Document.objects.all()
   context1={'documents': documents}
   if request.method == "POST":
      if request.POST['title']=="":
         messages.info(request,"Title cannot be empty!")
         return redirect("/")
      
      title=request.POST["title"]
      content=request.POST["content"]
      newnote = Document(title=title,content=content)
      newnote.save()
      messages.info(request,"Note Saved")
      request.user.note.add(newnote)
   
   return render(request,'index.html',context1)

def note_details(request,noteid):
   note = Document.objects.get(id=noteid)
   form = DocumentForm(instance=note)

   documents = Document.objects.all()
   context={'note':note,'form':form}
   return render(request,'notedetails.html',context)

def delete(request,noteid):
   note= get_object_or_404(Document,id=noteid)
   note.delete()
   return redirect("/")

def update(request,noteid):
   note = Document.objects.get(id=noteid)
   if request.method=="POST":
      form=DocumentForm(request.POST,instance=note)
      if form.is_valid():
         form.save()
         return redirect("/")
   else:
      form=DocumentForm(instance=note)
   return render(request,'update.html',{'form':form})
   
   
