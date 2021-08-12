from django.db import models


class Cliente(models.Model):
    REQUIRED_FIELDS = ('email', 'cpf')

    email = models.CharField(max_length=255, unique=True)
    cpf = models.CharField(max_length=11)

    @property
    def __str__(self):
        return self.email
