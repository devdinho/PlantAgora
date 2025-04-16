class ProfileType(object):
    """Object representando diferentes tipos de Perfis de Usuários.

    Atributos:
        - ADMIN (int): Administrador, usuário com permissões de administrador.
        - DEVELOPER (int): Desenvolvedor, usuário com permissões de desenvolvedor.
        - GARDENER (int): Hortelão/Produtor, usuário com permissões de hortelão/produtor.
    """

    ADMIN = 1
    DEVELOPER = 2
    GARDENER = 3

    PROFILE_TYPE_CHOICES = (
        (ADMIN, "Administrador"),
        (DEVELOPER, "Desenvolvedor"),
        (GARDENER, "Hortelão/Produtor"),
    )


class DocumentType(object):
    """Object representando diferentes tipos de Documentos.

    Atributos:
        - CPF (int): Cadastro de Pessoas Físicas, identificação do registro de contribuintes individuais no Brasil.
        - CNPJ (int): Cadastro Nacional da Pessoa Jurídica, identificação do registro de entidades legais no Brasil.
        - RG (int): Registro Geral, identificação geral no Brasil.
        - IE (int): Inscrição Estadual, registro estadual no Brasil.
        - IM (int): Inscrição Municipal, registro municipal no Brasil.
        - PASSPORT (int): Identificação de passaporte.
        - CNH (int): Carteira Nacional de Habilitação, carteira de motorista no Brasil.
        - CTPS (int): Carteira de Trabalho e Previdência Social, carteira de trabalho e previdência social no Brasil.
        - OTHER (int): Qualquer outro tipo de documento não listado acima.

    Observação:
        - Os valores dos atributos são inteiros e representam o tipo de documento
          de acordo com a lista acima. O campo que armazena o valor do documento é do tipo str.
    """

    CPF = 1
    CNPJ = 2
    OTHER = 0

    DOCUMENT_TYPE_CHOICES = (
        (CPF, "CPF"),
        (CNPJ, "CNPJ"),
        (OTHER, "Outro"),
    )


class Status(object):
    """Object representando diferentes status de objetos.

    Atributos:
        - ACTIVE (int): Ativo, objeto ativo.
        - INACTIVE (int): Inativo, objeto inativo.
    """

    ACTIVE = 1
    INACTIVE = 2

    STATUS_CHOICES = (
        (ACTIVE, "Ativo"),
        (INACTIVE, "Inativo"),
    )


class SignatureValidationMonths(object):
    """Object representando os meses de validade da assinatura.

    Atributos:
        - ONE_MONTH (int): Um mês de validade.
        - THREE_MONTHS (int): Três meses de validade.
        - SIX_MONTHS (int): Seis meses de validade.
        - TWELVE_MONTHS (int): Doze meses de validade.
    """

    ONE_MONTH = 1
    THREE_MONTHS = 3
    SIX_MONTHS = 6
    TWELVE_MONTHS = 12

    SIGNATURE_VALIDATION_MONTHS_CHOICES = (
        (ONE_MONTH, "Um mês"),
        (THREE_MONTHS, "Três meses"),
        (SIX_MONTHS, "Seis meses"),
        (TWELVE_MONTHS, "Doze meses"),
    )


class LevelOfEducation(object):
    """Object representando os níveis de escolaridade.

    Atributos:
        - BASIC (int): Educação infantil e Ensino Fundamental.
        - HIGH_SCHOOL (int): Ensino Médio.
        - UNDERGRADUATE (int): Graduação.
        - POSTGRADUATE (int): Pós-Graduação.
    """

    BASIC = 1
    HIGH_SCHOOL = 2
    UNDERGRADUATE = 3
    POSTGRADUATE = 4

    LEVEL_OF_EDUCATION_CHOICES = (
        (BASIC, "Ensino Fundamental"),
        (HIGH_SCHOOL, "Ensino Médio"),
        (UNDERGRADUATE, "Graduação"),
        (POSTGRADUATE, "Pós-Graduação"),
    )
