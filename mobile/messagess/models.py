from django.db import models

from users.models import CustomUser

# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="receiver")
    message = models.CharField(blank=True, null=True,max_length=200)
    image=models.ImageField(upload_to='messages/images/',blank=True,null=True)
    is_read=models.BooleanField(default=False)
    created_at = models.DateTimeField(
        verbose_name="created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="update at", auto_now=True)

    def __str__(self):
        if self.message!=None:
            return str(self.message)
        else:
            return str(self.image)