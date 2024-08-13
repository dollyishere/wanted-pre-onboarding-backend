from rest_framework import serializers
from ..models import Company

# company serializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_id', 'company_name', 'country', 'region']
