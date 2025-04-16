from django.db import models


class City(models.Model):
    """Modelo de cidade.
    Uma instância deste modelo representa uma cidade.

    Atributos:
        - name (str): Nome da cidade.
        - state (str): Estado da cidade.
    """

    name = models.CharField("Name", max_length=100)
    state = models.ForeignKey(
        "State",
        on_delete=models.CASCADE,
        verbose_name="State",
        related_name="cities",
        related_query_name="city",
    )

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return f"{self.name} - {self.state.abbreviation}"


class State(models.Model):
    """Modelo de estado.
    Uma instância deste modelo representa um estado.

    Atributos:
        - name (str): Nome do estado.
        - abbreviation (str): Sigla do estado.
    """

    name = models.CharField("Name", max_length=100)
    abbreviation = models.CharField("Abbreviation", max_length=2)

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"

    def __str__(self):
        return f"{self.name}({self.abbreviation})"
