from django.contrib.auth.models import User
from .models import Profile, City
from job_board_styleguide.common.services import model_update
from rest_framework.authtoken.models import Token




def profile_create(
    *,
    user:User,
    city: int,
    phonenumber: str,
    img: str,
    ) -> Profile:
    
    profile = Profile(user=user,city=city, phone_number=phonenumber, image=img)
    profile.full_clean()
    profile.save()
    return profile


def user_create(
    email: str,
    first_name: str,
    last_name: str,
    username:str,
    password: str,
    city: int,
    phonenumber: str,
    img: str
    ) -> User:
    
    user = User(email=email, username=username, first_name=first_name, last_name=last_name)
    user.set_password(password)
    user.full_clean()
    user.save()
    token = Token.objects.create(user=user)
    

    profile_create(user=user, city=city,
                   phonenumber=phonenumber, img=img)
    
    return user, token.key

def user_update(*, user_id: int, data) -> User:
    user = User.objects.get(id = user_id)
    non_side_effect_fields = ['first_name', 'last_name']

    user, has_updated = model_update(
        instance=user,
        fields=non_side_effect_fields,
        data=data
    )

    return user

def profile_update(*, profile_id: int, data):
    profile = Profile.objects.get(id = profile_id)
    non_side_effect_fields = ['city', 'phone_number', 'image']
    
    profile, has_updated = model_update(
        instance=profile,
        fields=non_side_effect_fields,
        data=data
    )

    return profile

    
    
