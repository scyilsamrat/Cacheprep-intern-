from rest_framework import serializers
from main.models import Questions
class Q_serializers(serializers.ModelSerializer):	
	Q_id=serializers.CharField(required=False)
	Q_text=serializers.CharField(required=False)
	Q_img=serializers.ImageField(required=False)
	Q_tag=serializers.CharField(required=False)
	class Meta:
		model=Questions
		#fields=('Q_id','Q_text','Q_img','Q_tag')
		fields='__all__'
