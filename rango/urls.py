from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    # path(<string to match>, <view to call>, <name, convenient way to reference view, optional>)
    path('',views.index, name='index'),
]

