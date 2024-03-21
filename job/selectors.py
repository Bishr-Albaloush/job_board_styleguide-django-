from .models import Job
import django_filters

def job_get(*,id):
    job = Job.objects.get(id = id)
    return job

def apply_get(*,id):
    apply = apply.objects.get(id = id)
    return apply

class JobFilter(django_filters.FilterSet):
    
    class Meta:
        model = Job
        fields = ('title', 'description')


def job_list(*, filters=None):
    filters = filters or {}

    qs = Job.objects.all()

    return JobFilter(filters, qs).qs