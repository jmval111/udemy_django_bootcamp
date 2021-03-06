from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from . import models
from django.core.urlresolvers import reverse_lazy

# Create your views here.
# Class-based-template-view
class IndexView(TemplateView):
    # Path to the template in `templates`.
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injected_content'] = 'BASIC INJECTION!'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'basic_app/school_list.html'

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ['name', 'principal', 'location']
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ['name', 'principal']
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')

# Class-based-view
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL")

# Function-based-view
# def index(request):
#     return render(request, 'index.html')
