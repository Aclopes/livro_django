from medicSearch.models import *
from django.db.models import Sum, Count

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICE, default=3)
    birthday = models.DateField(default=None, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    favorites = models.ManyToManyField(User, blank=True, related_name='favorites')
    speciality = models.ManyToManyField(Speciality, blank=True, related_name='speciality')
    addresses = models.ManyToManyField(Address, blank=True, related_name='addresses')
    image = models.ImageField(null=True, blank=True)


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
    

    def show_scoring_average(self):
        from .Rating import Rating
        try:
            ratings = Rating.objects.filter(user_rated=self.user).aggregate(Sum('value'), Count('user'))
            if ratings['user__count'] > 0:
                scoring_average = ratings['value__sum']/ratings['user__count']
                scoring_average = round(scoring_average, 2)
                return scoring_average
            return 'Sem Avaliação'
        except:
            return 'Sem avaliação'
    
