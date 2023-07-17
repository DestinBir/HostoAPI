from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Hospital import views

urlpatterns = [
    path('Hospitals/', views.HostoList.as_view()),
    path('Hospital/<int:pk>/', views.HostoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)