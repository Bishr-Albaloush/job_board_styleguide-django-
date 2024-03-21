from .models import Profile

def profile_get(*,id):
    profile = Profile.objects.get(id = id)
    return profile