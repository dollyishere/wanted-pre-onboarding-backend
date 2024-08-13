from .views import (
    RecruitmentViewSet, 
    CompanyViewSet, 
    UserViewSet, 
    ResumeViewSet
)


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
user_viewset = UserViewSet.as_view({
    'post' : 'create'
})
resume_viewset = ResumeViewSet.as_view({
    'get' : 'list',
    'post' : 'create',
})