from django.contrib.auth.models import User

user = User.objects.filter(pk=1).first()


def main_user(request):
    return {'main_user': user}


def main_user_info(request):
    return {'main_user_info': user.profileinfo}


def main_user_skills(request):
    return {'main_user_skills': user.profileinfo.profileskill_set.all()}


def main_user_socials(request):
    return {'main_user_socials': user.profileinfo.sociallink_set.all()}
