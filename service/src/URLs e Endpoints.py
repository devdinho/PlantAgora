"""

Painel Administrativo:
    - 'admin/' -> URL para acessar a interface do painel de administração.

Endpoints e seus payloads:
    - 'api/register/' -> Endpoint para registrar um novo usuário.
        ```json
            {
                "first_name": "string",
                "last_name": "string",
                "username": "string",
                "password": "string",
                "email": "string",
            }
        ```
    - 'api/login/' -> Endpoint para obter o token de acesso.
        ```json
            {
                "username": "string",
                "password": "string"
            }
        ```
    - 'api/login/refresh/' -> Endpoint para atualizar o token de acesso.
        ```json
            {
                "refresh": "string"
            }
        ```
"""
