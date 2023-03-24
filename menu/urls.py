from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('p<int:parent_number>', views.index, name='parent'),
    path('p<int:parent_number>/c<int:child_number>', views.index, name='child'),
    path('p<int:parent_number>/c<int:child_number>/s<int:subchild_number>', views.index, name='subchild'),
]
