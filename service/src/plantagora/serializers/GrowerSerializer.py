from rest_framework import serializers

from plantagora.models import Grower


class GrowerSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Grower (Hortelão)."""

    level_of_education = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()

    class Meta:
        model = Grower
        fields = [
            "id",
            "caf",
            "address",
            "level_of_education",
            "document",
            "gender",
            "birthDate",
            "cell",
            "registeredAt",
            "updatedAt",
            "registerApproved",
            "registerApprovedAt",
            "registerApprovedBy",
        ]
        read_only_fields = ["id"]

    def get_level_of_education(self, instance):
        """Retorna o nível de educação do Grower (Hortelão)."""
        return instance.get_levelOfEducation_display()

    def get_gender(self, instance):
        """Retorna o gênero do Grower (Hortelão)."""
        return instance.get_gender_display()
