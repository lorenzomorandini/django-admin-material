from django.db import models


class TestModel(models.Model):
    text_1 = models.CharField('text 1', max_length=50, blank=True)
    text_2 = models.CharField('text 2', max_length=50)


class Test2Model(models.Model):
    test = models.ForeignKey(TestModel, blank=True, null=True, on_delete=models.CASCADE)