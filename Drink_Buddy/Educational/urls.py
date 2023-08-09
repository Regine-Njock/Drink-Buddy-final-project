from django.urls import path
from . import views

app_name = 'Educational'

urlpatterns = [
    path('',views.all_educational, name='all_educational'),
    path('<int:Insight_id>/', views.detail, name='detail'),
   
]