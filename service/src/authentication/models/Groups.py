from django.contrib.auth.models import Group


class Groups(Group):
    class Meta:
        proxy = True
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"

    pass
