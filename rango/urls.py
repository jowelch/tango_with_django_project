from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    # path(<string to match>, <view to call>, <name, way to reference view, optional>)
    path('',views.index, name='index'),
    path('about/',views.about, name='about')
]

