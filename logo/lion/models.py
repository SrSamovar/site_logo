from django.db import models


class Teacher(models.Model):
    surname = models.CharField(max_length=30, verbose_name='Фамилия', null=True, blank=True)
    first_name = models.CharField(max_length=30, verbose_name='Имя', null=True, blank=True)
    last_name = models.CharField(max_length=30, verbose_name='Отчество', null=True, blank=True)
    work_experience = models.IntegerField(verbose_name='Опыт работы', null=True, blank=True)
    work_position = models.CharField(max_length=30, verbose_name='Должность', null=True, blank=True)

    def __str__(self):
        return f'{self.surname} {self.first_name} {self.last_name} - {self.work_position}'


class Child(models.Model):
    surname = models.CharField(max_length=30, verbose_name='Фамилия', null=True, blank=True)
    first_name = models.CharField(max_length=30, verbose_name='Имя', null=True, blank=True)
    last_name = models.CharField(max_length=30, verbose_name='Отчество', null=True, blank=True)
    age = models.IntegerField(default=1, verbose_name='Возраст', null=True, blank=True)

    def __str__(self):
        return f'{self.surname} {self.first_name} {self.last_name} - {self.age}'


class Club(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название кружка', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.price}'


class ChildClub(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['child', 'club', 'teacher']  # Уникальная связь между Child и Club

    def __str__(self):
        return f'{self.child} - {self.club}'

