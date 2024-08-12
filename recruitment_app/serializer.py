from rest_framework import serializers
from .models import Company, User, Recruitment, Resume

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_id', 'company_name', 'country', 'region']


class RecruitmentSerializer(serializers.ModelSerializer):
    company_id = serializers.PrimaryKeyRelatedField(source='company', queryset=Company.objects.all())

    class Meta:
        model = Recruitment
        fields = ['recruitment_id', 'company_id', 'position', 'compensation', 'content', 'skill']

class RecruitmentCreatedSerializer(serializers.ModelSerializer):
    company_id = serializers.PrimaryKeyRelatedField(source='company', queryset=Company.objects.all())
    compensation = serializers.IntegerField(default=0)

    class Meta:
        model = Recruitment
        fields = ['company_id', 'position', 'compensation', 'content', 'skill']


class RecruitmentListSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    region = serializers.SerializerMethodField()

    class Meta:
        model = Recruitment
        fields = ['recruitment_id', 'company_name', 'country', 'region', 'position', 'compensation', 'skill']


    def get_company_name(self, obj):
        return obj.company.company_name if obj.company else None

    def get_country(self, obj):
        return obj.company.country if obj.company else None

    def get_region(self, obj):
        return obj.company.region if obj.company else None
    
class RecruitmentDetailSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    region = serializers.SerializerMethodField()
    related_recruitments = serializers.SerializerMethodField()

    class Meta:
        model = Recruitment
        fields = ['recruitment_id', 'company_name', 'country', 'region', 'position', 'compensation', 'skill', 'content', 'related_recruitments']

    def get_company_name(self, obj):
        return obj.company.company_name if obj.company else None

    def get_country(self, obj):
        return obj.company.country if obj.company else None

    def get_region(self, obj):
        return obj.company.region if obj.company else None
    
    def get_related_recruitments(self, obj):
        company_id = obj.company_id
        # exclude now recruitment
        related_recruitments = Recruitment.objects.filter(company_id=company_id).exclude(pk=obj.pk)
        # .values_list() is some field's value get like list
        # flat can change a target list has only one field, can change it to a one-dimensional list
        return list(related_recruitments.values_list('recruitment_id', flat=True))
    
class RecruitmentUpdatedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recruitment
        fields = ['position', 'compensation', 'content', 'skill']