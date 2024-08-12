from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecruitmentViewSet, CompanyViewSet

router = DefaultRouter()
recruitment_viewset = RecruitmentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
recruitment_detail_viewset = RecruitmentViewSet.as_view({
    'get': 'retrieve',
    'put' : 'update',
    'delete': 'destroy'
})
company_viewset = CompanyViewSet.as_view({
    'post' : 'create'
})

router.register(r'recruitments', RecruitmentViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('company/', company_viewset, name="company"),
    path('recruitments/', recruitment_viewset, name='recruitment'),
    path('recruitments/<int:pk>/',  recruitment_detail_viewset, name='recruitment-detail'),
]

