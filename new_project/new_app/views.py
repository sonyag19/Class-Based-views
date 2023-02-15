from django.shortcuts import render,redirect
from django.views import generic
from .forms import *
from django.urls import reverse_lazy
from django.http import HttpResponse
import os

# Create your views here.

class regclass(generic.CreateView):
    form_class=regform
    template_name='register.html'
    success_url= reverse_lazy('login')

class logclass(generic.View):
    form_class=logform
    template_name='login.html'
    def get(self,request):
        form=self.form_class
        return render(request,'login.html',{'form':form})

    def post(self,request):
        if request.method =='POST':
            a=logform(request.POST)
            if a.is_valid():
                em=a.cleaned_data['email']
                ps=a.cleaned_data['password']
                b=regmodel.objects.all()
                for i in b:
                    if em==i.email and ps==i.password:
                        return HttpResponse("login success")
                else:
                    return HttpResponse("login failed")

# ListView
class listview(generic.ListView):
    model= regmodel
    template_name= 'display.html'
    def get(self,request):
        a=self.model.objects.all()
        return render(request,self.template_name,{'a':a})

# to delete
class deleteview(generic.DeleteView):
    model=regmodel
    template_name='delete.html'
    success_url=reverse_lazy('display')

#detail view
class detail(generic.DetailView):
    model=regmodel
    template_name='detail.html'


# Update View
class update(generic.UpdateView):
    model=regmodel
    template_name='update.html'
    fields=['username','email']
    success_url=reverse_lazy('display')

class fileClass(generic.CreateView):
    form_class=fileForm
    template_name='file.html'
    success_url=reverse_lazy("filedis")

####### Display File ###########
class filedis(generic.ListView):
    model=fileModel
    template_name='filedisplay.html'   
    def get(self,request):
        a=self.model.objects.all()
        image=[]
        name=[]
        id1=[]
        for i in a:
            id=i.id
            id1.append(id)
            im=str(i.image).split('/')[-1]
            image.append(im)
            nm=i.itemname
            name.append(nm)
        mylist=zip(image,name,id1)
        return render(request,self.template_name,{'a':mylist})       
        
###### Delete ######
class filedelete(generic.DeleteView):
    model=fileModel
    template_name='delete.html'
    success_url=reverse_lazy('filedis')

##### Detail #####
class filedetail(generic.DetailView):
    model=fileModel
    template_name='filedetail.html'
    def get(self,request,**kwargs):
        val=kwargs.get('pk')
        a=self.model.objects.get(id=val)
        b=a.itemname
        j=str(a.image).split('/')[-1]
        return render(request,'filedetail.html',{'j':j,'b':b})


class fileUpdate(generic.UpdateView):
    model=fileModel
    template_name='update.html'
    fields= '__all__'
    form_class=fileForm

    def get(self, request,**kwargs):
        a=self.form_class
        id1=kwargs.get('pk')
        a=self.model.objects.get(id=id1) 
        image=str(a.image).split('/')[-1]
        name=a.itemname
        return render(request,'update.html',{'image':image,'name':name})

    def post(self,request,**kwargs):
        id1=kwargs.get('pk')
        a=self.model.objects.get(id=id1) 
        image=str(a.image).split('/')[-1]
        print(image)
        name=a.itemname
        print(name)
        if request.method=='POST':
            if len(request.FILES) != 0:
                if len(a.image)>0:
                    os.remove(a.image.path)
                a.image=request.FILES['image']
            a.itemname=request.POST.get('itemname')
            a.save()
            return redirect('http://127.0.0.1:8000/new_app/displayfile')
        
            
        
            
                 
        