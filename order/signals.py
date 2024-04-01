from django.conf import settings
from django.dispatch import receiver
from .models import Order, TrackOrder
from django.core.mail import send_mail
from django.db.models.signals import post_save


@receiver(post_save, sender=Order)
def track_order_create_signals(sender, instance, created, **kwargs):
    if created:
        TrackOrder.objects.create(
            order=instance
        )
        message = f"Your order number {instance.invoice_id} has been received."
        send_mail(
            "Coffee Garden",
            message,
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=True
        )

