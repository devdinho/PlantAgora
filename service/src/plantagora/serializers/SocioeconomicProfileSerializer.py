from rest_framework import serializers


class SocioeconomicProfileSerializer(serializers.ModelSerializer):
  """Serializer para o modelo SocioeconomicProfile (Perfil Socioeconômico)."""

  class Meta:
    model = "SocioeconomicProfile"
    fields = [
      "id",
      "questionaire",
      "answers",
      "status",
      "submitted_at",
      "updatedAt",
    ]  
    read_only_fields = ["id", "updatedAt"]
  
  def get_questionaire(self, instance):
    """Retorna o questionário associado ao perfil socioeconômico."""
    return instance.questionaire.title if instance.questionaire else None  
            