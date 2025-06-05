from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListVIew, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Page
from .forms import PageForm

# Create your views here.


class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'
    
    
class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_create.html'
    success_url = reverse_lazy('page_list')


    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_update.html'
    success_url = reverse_lazy('page_list')


class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_delete.html'
    success_url = reverse_lazy('page_list')
