from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class GetUserUsernameRestView(APIView):
  """Endpoint para receber o nome de usuário.

    Parâmetros:
      - Method: GET
      - Headers: 
      ```json
        { 
          Authorization: Bearer <token> 
        }
      ```
  """
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]

  def get(self, request):
      content = {'username': request.user.username}
      return Response(content)