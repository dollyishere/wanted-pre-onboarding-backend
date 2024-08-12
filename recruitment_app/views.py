from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from django.db.models import Q
from .models import Company, User, Recruitment, Resume
from .serializer import RecruitmentListSerializer, RecruitmentCreatedSerializer, RecruitmentDetailSerializer, RecruitmentUpdatedSerializer, CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def create(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class RecruitmentViewSet(viewsets.ModelViewSet):
    queryset = Recruitment.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RecruitmentCreatedSerializer
        elif self.request.method == 'PUT' or self.request.method == 'PATCH':
            return RecruitmentUpdatedSerializer
        elif self.request.method == 'GET':
            if self.action == 'retrieve':
                return RecruitmentDetailSerializer
            return RecruitmentListSerializer
        return super().get_serializer_class()
    
    def list(self, request):
        queryset = Recruitment.objects.all()
        serializer = RecruitmentListSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def filter_queryset(self, queryset):
        search_params = {
            'company_name': self.request.query_params.get('company_name', None),
            'country': self.request.query_params.get('country', None),
            'region': self.request.query_params.get('region', None),
            'position': self.request.query_params.get('position', None),
            'compensation': self.request.query_params.get('compensation', None),
            'skill': self.request.query_params.get('skill', None)
        }

        filters = Q()
        for key, value in search_params.items():
            if value:
                if key in ['compensation']:
                    filters &= Q(**{f'{key}__exact': value})
                else:
                    filters &= Q(**{f'company__{key}__icontains': value}) | Q(**{f'{key}__icontains': value})

        return queryset.filter(filters)
    
    def create(self, request):
        serializer = RecruitmentCreatedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def retrieve(self, request, pk=None):

        try:
            recruitment = Recruitment.objects.get(pk=pk)
        except Recruitment.DoesNotExist:
            return Response(status=404)
        serializer = RecruitmentDetailSerializer(recruitment)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            recruitment = Recruitment.objects.get(pk=pk)
        except Recruitment.DoesNotExist:
            return Response(status=404)
        serializer = RecruitmentUpdatedSerializer(recruitment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            recruitment = Recruitment.objects.get(pk=pk)
        except Recruitment.DoesNotExist:
            return Response(status=404)
        recruitment.delete()
        return Response(status=204)