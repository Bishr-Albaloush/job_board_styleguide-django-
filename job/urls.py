from django.urls import path, include
from . import api
app_name = 'job'
urlpatterns = [
    path('api/v1/job_create/', api.JobCreateApi.as_view(),name='job_create'),
    path('api/v1/apply_get/', api.ApplyDetailApi.as_view(),name='apply_get'),
    path('api/v1/job_list/',api.JobListApi.as_view(),name='job_list'),
    path('api/v1/apply_create/',api.ApplyCreateApi.as_view(),name='apply_create'),
    path('api/v1/job_update/<int:job_id>',api.JobUpdateApi.as_view(),name='job_update'),
    path('api/v1/job_get/',api.JobDetailApi.as_view(),name='job_get'),
]