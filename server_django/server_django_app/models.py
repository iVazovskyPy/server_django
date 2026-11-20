from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class Position(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Должность')

    def __str__(self):
        return self.title


class Unit(models.Model):
    class UnitType(models.TextChoices):
        SERVICE = 'service', 'Служба'
        DEPARTMENT = 'department', 'Отдел'
        SECTOR = 'sector', 'Сектор'

    name = models.CharField(max_length=200, verbose_name='Название')
    unit_type = models.CharField(
        max_length = 20,
        choices = UnitType.choices,
        verbose_name = 'Тип подразделения'
    )
    parent = models.ForeignKey(
        'self',
        on_delete = models.CASCADE,
        null = True,
        blank = True,
        related_name = 'children',
        verbose_name = 'Вышестоящее подразделение'
    )

    def clean(self):
        if self.unit_type == self.UnitType.SERVICE and self.parent is not None:
            raise ValidationError('У службы не может быть вышестоящего подразделения')
        if self.unit_type == self.UnitType.DEPARTMENT and (not self.parent or self.parent.unit_type != self.UnitType.SERVICE):
            raise ValidationError('Отдел должен входить в состав службы')
        if self.unit_type == self.UnitType.SECTOR and (not self.parent or self.parent.unit_type != self.UnitType.DEPARTMENT):
            raise ValidationError('Сектор должен входить в состав отдела')

    def __str__(self):
        return f"{self.get_unit_type_display()}.{self.name}"

class Employee(AbstractUser):
    #Стандартные поля (username, email, password, first_name, last_name)
    middle_name = models.CharField(max_length=100, blank=True, default='', verbose_name='Отчество')
    unit = models.ForeignKey(
        Unit,
        on_delete = models.PROTECT,
        blank = True,
        null = True,
        related_name = 'employees',
        verbose_name = 'Подразделение'
    )
    position = models.ForeignKey(
        Position,
        on_delete = models.PROTECT,
        blank = True,
        null = True,
        related_name = 'employees',
        verbose_name = 'Должность'
    )
