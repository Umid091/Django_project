from django.db import models

class Phone(models.Model):
    title = models.CharField(max_length=255,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PhoneImage(models.Model):
    phone =models.ForeignKey(Phone,  on_delete=models.CASCADE , related_name='images',)
    image = models.ImageField(upload_to='phones/', verbose_name="Rasm")

    def __str__(self):
        return f"{self.phone.title}"
