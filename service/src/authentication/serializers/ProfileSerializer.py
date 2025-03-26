from rest_framework import serializers

from authentication.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
  """ Serializer para o modelo de usuário.
      
      ### Utilizado para converter objetos de usuário em JSON e vice-versa.
      
      Campos:
      - id: Identificador único do usuário.
      - first_name: Primeiro nome do usuário.
      - last_name: Último nome do usuário.
      - username: Nome de usuário.
      - password: Senha do usuário.
      - email: Endereço de e-mail do usuário.
      - last_login: Data e hora do último login do usuário.
      - date_joined: Data e hora de criação do usuário.
  """
  class Meta:
    model = Profile
    fields = ('id', 'first_name', 'last_name', 'username', 'password', 'email', 'last_login', 'date_joined')
    extra_kwargs = {
        'password': {'write_only':True}
    }
        
  def create(self, validated_data):
    newProfile = Profile(
      username = validated_data['username'],
      first_name = validated_data['first_name'],
      last_name = validated_data['last_name'],
      email = validated_data['email'],
    )

    newProfile.set_password(validated_data['password'])
    newProfile.save()

    return newProfile