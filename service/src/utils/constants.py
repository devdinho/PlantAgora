from enum import Enum


class ProfileType(Enum):
    """Enum representando diferentes tipos de Perfis de Usuários.

    Atributos:
        ADMIN (int): Administrador, usuário com permissões de administrador.
        DEVELOPER (int): Desenvolvedor, usuário com permissões de desenvolvedor.
        GARDENER (int): Hortelão/Produtor, usuário com permissões de hortelão/produtor.
    """

    ADMIN = 1
    DEVELOPER = 2
    GARDENER = 3


class DocumentType(Enum):
    """Enum representando diferentes tipos de Documentos.

    Atributos:
        CPF (int): Cadastro de Pessoas Físicas, identificação do registro de contribuintes individuais no Brasil.
        CNPJ (int): Cadastro Nacional da Pessoa Jurídica, identificação nacional do registro de entidades legais no Brasil.
        RG (int): Registro Geral, identificação geral no Brasil.
        IE (int): Inscrição Estadual, registro estadual no Brasil.
        IM (int): Inscrição Municipal, registro municipal no Brasil.
        PASSPORT (int): Identificação de passaporte.
        CNH (int): Carteira Nacional de Habilitação, carteira de motorista no Brasil.
        CTPS (int): Carteira de Trabalho e Previdência Social, carteira de trabalho e previdência social no Brasil.
        OTHER (int): Qualquer outro tipo de documento não listado acima.
    """

    CPF = 1
    CNPJ = 2
    RG = 3
    IE = 4
    IM = 5
    PASSPORT = 6
    CNH = 7
    CTPS = 8
    OTHER = 9


class Status(Enum):
    """Enum representando diferentes status de objetos.

    Atributos:
        ACTIVE (int): Ativo, objeto ativo.
        INACTIVE (int): Inativo, objeto inativo.
    """

    ACTIVE = 1
    INACTIVE = 2
