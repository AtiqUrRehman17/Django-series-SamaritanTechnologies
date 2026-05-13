from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_stuff, name='all_stuff'),
    path('chai_store/',views.store_view,name='chai_store')
]
