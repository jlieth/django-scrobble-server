from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from scrobble_server.core.models.profile import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def get_or_create_profile_on_user_save(sender, instance, **kwargs):
    Profile.objects.get_or_create(user=instance)


@receiver(post_delete, sender=Profile)
def create_new_profile_if_user_still_exists(sender, instance, **kwargs):
    user = instance.user
    # user still in db?
    user_exists = User.objects.filter(pk=user.pk).exists()
    # if so, create new p and attach it to the user
    if user_exists:
        Profile.objects.create(user=user)
