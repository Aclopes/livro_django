from medicSearch.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICE, default=3)
    byrthday = models.DateField(default=None, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    favorites = models.ManyToManyField(User, blank=True, related_name='favorites')
    speciality = models.ManyToManyField(Speciality, blank=True, related_name='speciality')
    addresses = models.ManyToManyField(Address, blank=True, related_name='addresses')


    def __str__(self) -> str:
        return '{}'.format(self.user.username)


    @receiver(post_save, sender=user)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            Profile.objects.create(user=instance)
        except:
            pass

    
    @receiver(post_save, sender=user)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass