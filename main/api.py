
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class Q_list(APIView):
	def get(self,request):
		#tag=self.request.tag
		#model= Questions.objects.filter(Q_tag=tag)
		model=Questions.objects.all()
		serializer=Q_serializers(model,many=True)
		return Response(serializer.data)

	def post(self,request):
		parser_class = (FileUploadParser,)
		serializer=Q_serializers(data=request.data)
		if(serializer.is_valid()):
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)	
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Q(APIView):
	def get(self,request,Q_id):
		#tag=self.request.tag
		#model= Questions.objects.filter(Q_tag=tag)
		try:
			model=Questions.objects.get(id=Q_id)
		except Questions.DoesNotExist:
			return Response(f'Question with {Q_id} does not found in database',status=status.HTTP_404_NOT_FOUND)
		serializer=Q_serializers(model)
		return Response(serializer.data)

	def put(self,request,Q_id):
		try:
			model=Questions.objects.get(id=Q_id)
		except Questions.DoesNotExist:
			return Response(f'Question with {Q_id} does not found in database',status=status.HTTP_404_NOT_FOUND)
		parser_class = (FileUploadParser,)

		serializer=Q_serializers(data=request.data)
		if(serializer.is_valid()):
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)	
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)