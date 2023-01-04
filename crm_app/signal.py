from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from crm_app.models import CustomUser,AdminHOD,Agent,Customer



@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created: 
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Agent.objects.create(admin=instance)
        if instance.user_type==3:
            Customer.objects.create(admin=instance)



@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.agent.save()
    if instance.user_type==3:
        instance.customer.save()
    


