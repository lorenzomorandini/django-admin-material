from django.db import models


CHOICES_1 = (
    ('1', 'One'),
    ('2', 'Two'),
    ('3', 'Three'),
    ('4', 'Four'),
    ('5', 'Five')
)


class Model1(models.Model):
    text_1 = models.CharField('text 1', max_length=50, blank=True)
    text_2 = models.CharField('text 2', max_length=50)
    choice_1 = models.CharField('choice 1', max_length=50, choices=CHOICES_1)
    boolean_1 = models.BooleanField('boolean 1', default=False)

    def __str__(self):
        return '{} #{}'.format(self.text_2, self.pk)


class Model2(models.Model):
    test = models.ForeignKey(Model1, blank=True, null=True, on_delete=models.CASCADE)
    test_2 = models.ForeignKey(Model1, blank=True, null=True, on_delete=models.CASCADE, related_name='test2s')
    test_3 = models.ForeignKey(Model1, blank=True, null=True, on_delete=models.CASCADE, related_name='test3s')


class Model3(models.Model):
    test_4 = models.ForeignKey(Model1, blank=True, null=True, on_delete=models.CASCADE)
    text = models.CharField('text', max_length=50, blank=True)
    text_2 = models.CharField('text 2', max_length=50, blank=True, choices=CHOICES_1)