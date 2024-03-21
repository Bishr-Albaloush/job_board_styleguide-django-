from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from job_board_styleguide.accounts.models import User
from .models import Category
from .services import job_create
from .selectors import job_get

class JobCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
        title = serializers.CharField(max_length=100)
        job_type = serializers.CharField(max_length=15, choices=(
            ("Full Time", "Full Time"),
            ("Part Time", "Part Time"),
        )
        )
        description = serializers.TextField(max_length=1000)
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
        user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
        city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
        image = serializers.ImageField()

    def get(self, request, profile_id):
        course = job_get(id=profile_id)

        serializer = self.OutputSerializer(course)

        return Response(serializer.data)
