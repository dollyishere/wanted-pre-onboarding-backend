from django.urls import path
from .viewset_case import (
    recruitment_viewset,
    recruitment_detail_viewset,
    company_viewset,
    user_viewset,
    resume_viewset
)

urlpatterns = [
    path('company/', company_viewset, name="company"),
    path('user/', user_viewset, name="user"),
    path('resume/', resume_viewset, name="resume"),
    path('recruitments/', recruitment_viewset, name='recruitment'),
    path('recruitments/<int:pk>/',  recruitment_detail_viewset, name='recruitment-detail'),
]

