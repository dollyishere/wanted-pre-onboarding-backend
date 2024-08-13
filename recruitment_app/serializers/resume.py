from rest_framework import serializers
from ..models import User, Recruitment, Resume

# resume serializer
class ResumeSerializer(serializers.ModelSerializer):
    recruitment_id = serializers.PrimaryKeyRelatedField(source="recruitment", queryset=Recruitment.objects.all())
    user_id = serializers.PrimaryKeyRelatedField(source="user", queryset=User.objects.all())

    class Meta:
        model = Resume
        fields = ['resume_id', 'recruitment_id', 'user_id']

    def validate(self, data):
        user = data.get('user')
        recruitment = data.get('recruitment')

        if Resume.objects.filter(user=user, recruitment=recruitment).exists():
            raise serializers.ValidationError("이미 지원한 채용공고입니다.")
        return data