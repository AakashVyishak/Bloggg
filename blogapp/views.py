from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from blogapp.models import blog
from django.urls import reverse_lazy

class home(ListView):
    model=blog
    template_name = "home.html"
    context_object_name = 'k'
class detail(DetailView):
    model=blog
    template_name = "detail.html"
    context_object_name = 'i'
class update(UpdateView):
    model=blog
    template_name = 'update.html'
    context_object_name = 'k'
    fields=('blog_id','blogname','desc','image')
    success_url = reverse_lazy('home')
    # def get_success_url(self):
    #     return reverse_lazy('detail', kwargs={'pk': self.object.id})
class deleto(DeleteView):
    model=blog
    template_name = 'delete.html'
    success_url=reverse_lazy('home')

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        id = request.POST.get('id')
        desc= request.POST.get('desc')
        image = request.FILES['image']
        p=blog(blog_id=id,blogname=name,desc=desc,image=image)
        p.save()
        return redirect('/')
    return render(request,"add.html")