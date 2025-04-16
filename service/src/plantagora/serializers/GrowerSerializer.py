from rest_framework import serializers

from plantagora.models import Grower


class GrowerSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Grower (Hortelão)."""

    level_of_education = serializers.SerializerMethodField()
    document_type = serializers.SerializerMethodField()

    class Meta:
        model = Grower
        fields = [
            "id",
            "caf",
            "address",
            "level_of_education",
            "document",
            "document_type",
        ]
        read_only_fields = ["id"]

    def get_level_of_education(self, instance):
        """Retorna o nível de educação do Grower (Hortelão)."""
        return instance.get_levelOfEducation_display()

    def get_document_type(self, instance):
        """Retorna o tipo de documento do Grower (Hortelão)."""
        return instance.get_documentType_display()
