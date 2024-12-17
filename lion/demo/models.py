from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст')
    position = models.CharField(max_length=100, verbose_name='Должность')

    def __str__(self):
        return f'Name{self.name}, age {self.age}, position {self.position}'


class Child(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст')

    teachers = models.ManyToManyField(Teacher, through='Club', related_name='children')


class Club(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='clubs')
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='clubs')


