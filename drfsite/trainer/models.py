from django.db import models

# Create your models here.
class Trainer(models.Model):
    name= models.CharField(max_length=50)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    spec = models.ForeignKey('Specialization', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name= "Тренер"
        verbose_name_plural ="Тренери"


class Specialization(models.Model):
    status= models.CharField(max_length=100)

    def __str__(self):
        return self.status