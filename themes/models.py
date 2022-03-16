from statistics import mode
from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=1000)
    theory = models.CharField(max_length=1000)
    video = models.CharField(max_length=1000)
    matches = models.CharField(max_length=1000)
    missing_word = models.CharField(max_length=1000)
    right_order = models.CharField(max_length=1000)
    right_answer = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self) -> str:
        return self.name