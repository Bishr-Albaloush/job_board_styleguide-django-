from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Category, Job
from .services import job_create, job_update, apply_create
from .selectors import job_get, apply_get
from job_board_styleguide.api.pagination import get_paginated_response, LimitOffsetPagination
from .selectors import job_list


class JobCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
        title = serializers.CharField(max_length=100)
        job_type = serializers.CharField(max_length=15
        )
        description = serializers.CharField(max_length=1000)
        published_at = serializers.DateTimeField()
        vacancy = serializers.IntegerField(default=1)
        salary = serializers.IntegerField(default=0)
        experince = serializers.IntegerField(default=1)
        Category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
        image = serializers.ImageField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        job_create(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)

class JobDetailApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
        title = serializers.CharField(max_length=100)
        job_type = serializers.CharField(max_length=15)
        description = serializers.CharField(max_length=1000)
        published_at = serializers.DateTimeField()
        vacancy = serializers.IntegerField(default=1)
        salary = serializers.IntegerField(default=0)
        experince = serializers.IntegerField(default=1)
        Category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
        image = serializers.ImageField()

    def get(self, request, job_id):
        job = job_get(id=job_id)

        serializer = self.OutputSerializer(job)

        return Response(serializer.data)

class JobUpdateApi(APIView):
    
    class InputSerializer(serializers.Serializer):
        title = serializers.CharField(max_length=100)
        job_type = serializers.CharField(max_length=15)
        description = serializers.CharField(max_length=1000)
        published_at = serializers.DateTimeField()
        vacancy = serializers.IntegerField(default=1)
        salary = serializers.IntegerField(default=0)
        experince = serializers.IntegerField(default=1)
        Category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
        image = serializers.ImageField()
        
  

    def post(self, request, job_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        job_update(job_id=job_id, data = serializer.validated_data)

        return Response(status=status.HTTP_200_OK)

class ApplyCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all())
        name = serializers.CharField(max_length=50)
        
        
        email = serializers.CharField(max_length=1000)
        created_at = serializers.DateTimeField()
        website = serializers.URLField()
        cv = serializers.FileField()
        cover_letter = serializers.CharField(max_length=500)
        
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        apply_create(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


    
class JobListApi(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 3

    class FilterSerializer(serializers.Serializer):
        title = serializers.CharField(required=False)
        description = serializers.CharField(required=False)
        
    class OutputSerializer(serializers.Serializer):
        title = serializers.CharField()
        description = serializers.CharField()

    def get(self, request):
        # Make sure the filters are valid, if passed
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        jobs = job_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=jobs,
            request=request,
            view=self
        )




class ApplyDetailApi(APIView):
    class OutputSerializer(serializers.Serializer):
        job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all())
        name = serializers.CharField(max_length=50)
        email = serializers.CharField(max_length=1000)
        created_at = serializers.DateTimeField()
        website = serializers.URLField()
        cv = serializers.FileField()
        cover_letter = serializers.CharField(max_length=500)
        
    def get(self, request, apply_id):
        apply = apply_get(id=apply_id)

        serializer = self.OutputSerializer(apply)

        return Response(serializer.data)
