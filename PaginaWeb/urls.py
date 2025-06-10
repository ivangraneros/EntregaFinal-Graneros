from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView, profile_edit_view, SignUpView, CustomLoginView, CustomLogoutView, profile_view, CustomPasswordChangeView, AboutView, InicioView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('inicio/',InicioView.as_view(), name = 'inicio'),
    path('about/', AboutView.as_view(), name='about'),

    #pages
    path('pages/', PageListView.as_view(), name = 'page_list'),
    path('pages/create/', PageCreateView.as_view(), name = 'page_create'),
    path('pages/<int:pk>/', PageDetailView.as_view(), name = 'page_detail'),
    path('pages/<int:pk>/update/', PageUpdateView.as_view(), name = 'page_update'),
    path('pages/<int:pk>/delete/', PageDeleteView.as_view(), name = 'page_delete'),

#perfil
    
    path('login/', CustomLoginView.as_view(), name= 'login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('perfil/', profile_view, name='perfil'),
    path('perfil/edit/', profile_edit_view, name='perfil_edit'),
    path('perfil/password/', CustomPasswordChangeView.as_view(), name='password_change'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
