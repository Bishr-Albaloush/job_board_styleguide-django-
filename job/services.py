from .models import Job, Apply
from datetime import date
from job_board_styleguide.common.services import model_update

def job_create(
        owner: int,
        title: str,
        job_type: str,
        description: str,
        published_at: date,
        vacancy: int,
        salary: int,
        experince: int,
        Category: int,
        img: str
):

    job = Job(owner=owner, title=title,
              job_type=job_type, description=description, published_at=published_at, vacancy=vacancy, salary=salary, experince=experince, Category=Category, img=img)
    job.full_clean()
    job.save()

def job_update(*, user_id: int, data) -> Job:
    job = Job.objects.get(id = user_id)
    non_side_effect_fields = ['title', 'job_type', 'description', 'vacancy', 'salary', 'experince', 'Category', 'image']

    user, has_updated = model_update(
        instance=user,
        fields=non_side_effect_fields,
        data=data
    )

    return user

def apply_create(job: int,
        name: str,
        email: str,
        website: str,
        cv: str,
        cover_letter: str,
)->Apply:
    apply = Apply(name=name, email=email,
              website=website, cv=cv, cover_letter=cover_letter)
    apply.full_clean()
    apply.save()