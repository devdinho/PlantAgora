from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from utils.constants import ProfileType


class Profile(AbstractUser):
    """
    Modelo de perfil de usuário personalizado.

    O perfil de usuário é baseado no modelo de usuário padrão do Django, mas com
    campos adicionais.
    """

    profileType = models.CharField(
        "Tipo de Perfil",
        max_length=1,
        choices=[(profileType.value, profileType.name) for profileType in ProfileType],
        default=ProfileType.GARDENER.value,
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name="Grupos de Permissões",
        blank=True,
        help_text="Os grupos aos quais este usuário pertence.",
        related_name="usuario_set",
        related_query_name="usuario",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="Permissões de Usuários",
        blank=True,
        help_text="Permissões específicas para este usuário.",
        related_name="usuario_permissions",
        related_query_name="usuario",
    )

    def __str__(self):
        return f"{self.get_full_name()} ({self.username})"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
