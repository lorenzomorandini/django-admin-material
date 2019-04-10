from django.db import models


CHOICES_1 = (
    ('1', 'One'),
    ('2', 'Two'),
    ('3', 'Three'),
    ('4', 'Four'),
    ('5', 'Five')
)


class TestModel(models.Model):
    text_1 = models.CharField('text 1', max_length=50, blank=True)
    text_2 = models.CharField('text 2', max_length=50)
    choice_1 = models.CharField('choice 1', max_length=50, choices=CHOICES_1)
    boolean_1 = models.BooleanField('boolean 1', default=False)

    def __str__(self):
        return '{} #{}'.format(self.text_2, self.pk)


class Test2Model(models.Model):
    test = models.ForeignKey(TestModel, blank=True, null=True, on_delete=models.CASCADE)
    test_2 = models.ForeignKey(TestModel, blank=True, null=True, on_delete=models.CASCADE, related_name='test2s')
