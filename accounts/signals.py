from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import CustomUser  


previous_is_active = None

@receiver(pre_save, sender=CustomUser)
def save_previous_state(sender, instance, **kwargs):
    global previous_is_active
    if instance.id:  
        previous_is_active = CustomUser.objects.get(id=instance.id).is_active

@receiver(post_save, sender=CustomUser)
def send_activation_email(sender, instance, created, **kwargs):
    global previous_is_active

    if created:
        return  

    
    if previous_is_active is False and instance.is_active:
        subject = "حساب شما فعال شد"
        message = f"سلام {instance.username},\n\nحساب کاربری شما با موفقیت فعال شد. می‌توانید وارد شوید."
        from_email = settings.EMAIL_HOST_USER
        reception_list = [instance.email]

        try:
            send_mail(subject, message, from_email, reception_list)
        except Exception as e:
            print(f"Error sending email: {e}")
