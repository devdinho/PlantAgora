from datetime import datetime

from rest_framework import serializers

from authentication.models import Profile
from plantagora.models import BaseAddress, Grower
from plantagora.serializers import GrowerSerializer
from utils.exceptions import SimpleDetailError
from utils.models import City


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer para o modelo de usuário.

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

    grower = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "password",
            "email",
            "profileType",
            "profilePicture",
            "grower",
            "last_login",
            "date_joined",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"validators": []},
            "email": {"validators": []},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance or (isinstance(self.instance, list) and not self.instance):
            self.fields["password"].required = True
        else:
            self.fields["password"].required = False

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)

        if "password" in validated_data:
            instance.set_password(validated_data["password"])

        instance.save()

        return instance

    def get_grower(self, instance):
        """Retorna o Grower associado ao usuário."""
        objects = Grower.objects.filter(profile=instance)
        return GrowerSerializer(objects, many=True).data[0] if objects else None


class RegisterSerializer(serializers.Serializer):
    fullname = serializers.CharField(write_only=True)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    document = serializers.CharField(write_only=True)
    birthdate = serializers.CharField(write_only=True)
    cell = serializers.CharField(write_only=True)
    zipcode = serializers.CharField(write_only=True)
    gender = serializers.IntegerField(write_only=True)
    scholarity = serializers.IntegerField(write_only=True)
    fulladdress = serializers.CharField(write_only=True)
    city = serializers.CharField(write_only=True)

    def create(self, validated_data):
        print(f"Data: {validated_data}")

        if Profile.objects.filter(username=validated_data["username"]).exists():
            raise SimpleDetailError("Document already exists")

        first_name = validated_data.get("fullname", "").split(" ").pop(0)
        last_name = " ".join(validated_data.get("fullname", "").split(" ")[1:])

        newProfile = Profile(
            username=validated_data["username"],
            first_name=first_name,
            last_name=last_name,
        )
        newProfile.set_password(validated_data["password"])

        newProfile.save()

        address = validated_data.get("fulladdress")

        print(f'City: {validated_data.get("city")}')
        print(f"Address: {address}")

        city = validated_data.get("city").split("/")[0].strip()

        newAddress = BaseAddress(
            street=address.split(",")[0].strip(),
            number=address.split(",")[1].strip(),
            complement=(
                address.split(",")[2].strip() if len(address.split(",")) > 2 else ""
            ),
            zip_code=validated_data.get("zipcode"),
            city=City.objects.get(
                name=city,
                state__abbreviation=validated_data.get("city").split("/")[-1].strip(),
            ),
        )

        newAddress.save()

        newGrower = Grower(
            address=newAddress,
            levelOfEducation=validated_data.get("scholarity"),
            document=validated_data.get("username"),
            gender=validated_data.get("gender"),
            cell=validated_data.get("cell"),
            profile=newProfile,
            birthDate=datetime.strptime(
                validated_data.get("birthdate"), "%d/%m/%Y"
            ).date(),
        )
        newGrower.save()

        return newProfile
