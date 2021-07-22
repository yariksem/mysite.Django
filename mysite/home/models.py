from django.db import models


class MyModels(models.Model):
    name = models.CharField(verbose_name='Name', max_length=60)
    description = models.TextField(verbose_name='Description', blank=True)
    desck = models.CharField(verbose_name="faskt description", max_length=60)


