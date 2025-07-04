from rest_framework import serializers


class SocioeconomicQuestionnaireSerializer(serializers.ModelSerializer):
    """Serializer para o modelo SocioeconomicQuestionnaire (Questionário Socioeconômico)."""

    class Meta:
        model = "SocioeconomicQuestionnaire"
        fields = [
            "id",
            "title",
            "description",
            "questions",
            "status",
            "releasedAt",
            "updatedAt",
        ]
        read_only_fields = ["id", "releasedAt", "updatedAt"]

    def get_questions(self, instance):
        """Retorna as perguntas do questionário."""
        return instance.questions if instance.questions else {}
