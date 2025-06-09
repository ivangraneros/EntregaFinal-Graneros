from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Page, UserAvatar
from .forms import PageForm, UserRegisterForm, UserProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

#CRUD

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


#vista de about

class AboutView(TemplateView):
    template_name = 'Paginaweb/pages/about.html'



class InicioView(TemplateView):
    template_name = 'pages/inicio.html'


#vista de perfil-acciones del perfil


class SignUpView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')


@login_required
def profile_view(request):
    return render(request, 'accounts/perfil.html')


@login_required
def profile_edit_view(request):
    if request_method == 'POST':
        form = UserProfileForm(request.POST, required.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'accounts/editar_perfil.html', {'form':form})


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/cambiar_contraseña.html'
    success_url = reverse_lazy('perfil')