from django.rls import path
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView

urlpatterns = [
    path('', PageListView.as_view(), name = 'inicio'),
    path('pages/', PageListVIew.as_view(), name = 'page_list'),
    path('pages/<int:pk>/', PageDetailView.as_view(), name = 'page_detail'),
    path('pages/create', PageCreateView.as_view(), name = 'page_create'),
    path('pages/<int:pk>/update/', PageUpdateView.as_view(), name = 'page_update'),
    path('pages/<int:pk>/delete/', PageDeleteView.as_view(), name = 'page_delete'),
]
