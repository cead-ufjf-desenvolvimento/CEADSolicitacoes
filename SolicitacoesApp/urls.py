from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('producao/new/', views.ProducaoDeMaterialCreateView.as_view(), name="producao_create"),
    path('404', views.Error404View, name="404")
]
