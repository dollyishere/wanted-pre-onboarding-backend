from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from django.db.models import Q
from .models import Company, User, Recruitment, Resume

from .serializers.company import ( CompanySerializer,)
from .serializers.user import (UserSerializer,)
from .serializers.resume import (ResumeSerializer,)
from .serializers.recruitment import (
    RecruitmentListSerializer,
    RecruitmentCreatedSerializer,
    RecruitmentDetailSerializer,
    RecruitmentUpdatedSerializer,
)

# company ViewSet
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # create new company
    def create(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# user ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # create new user
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# resume ViewSet
class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    # create new resume
    def create(self, request, *args, **kwarges):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def list(self, request):
        queryset = Resume.objects.all()
        serializer = ResumeSerializer(queryset, many=True)
        return Response(serializer.data)

# 채용 공고 ViewSet
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
    
    # 공고 목록 조회(검색 가능 => query string : search)
    def list(self, request):
        # get search value
        search_query = request.query_params.get('search', None)
        queryset = Recruitment.objects.all()

        if search_query:
            # if search_query can change int type, change type and input to search_compensation
            try:
                search_compensation = int(search_query)
            except ValueError:
                search_compensation = None

            queryset = queryset.filter(
                # icontans => case-free
                Q(company__company_name__icontains=search_query) |
                Q(company__country__icontains=search_query) |
                Q(company__region__icontains=search_query) |
                Q(position__icontains=search_query) |
                # search_compensation is not None, can search
                (Q(compensation=search_compensation) if search_compensation is not None else Q()) |
                Q(skill__icontains=search_query)
            )
        serializer = RecruitmentListSerializer(queryset, many=True)
        return Response(serializer.data)
    
    # 공고 신규 등록
    def create(self, request):
        serializer = RecruitmentCreatedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    # 단 건 조회
    def retrieve(self, request, pk=None):
        try:
            recruitment = Recruitment.objects.get(pk=pk)
        except Recruitment.DoesNotExist:
            return Response(status=404)
        serializer = RecruitmentDetailSerializer(recruitment)
        return Response(serializer.data)

    # 수정
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

    # 삭제
    def destroy(self, request, pk=None):
        try:
            recruitment = Recruitment.objects.get(pk=pk)
        except Recruitment.DoesNotExist:
            return Response(status=404)
        recruitment.delete()
        return Response(status=204)