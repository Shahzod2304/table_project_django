from django.urls import path 
from .views import Home, load_form,add,show, edit


urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('load_form',load_form, name='load_form'),
    path('add', add, name='add'),
    path('show', show, name='show'),
    path('edit/<int:id>', edit, name='edit'),
    # path('update/<int:id>', update, name='update'),
    

]