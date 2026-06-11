from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import AccessToken

from apps.accounts.services.token_blacklist import blacklist_token


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        token = request.auth

        access_token = AccessToken(str(token))

        jti = access_token["jti"]

        ttl = (
            access_token["exp"]
            - access_token["iat"]
        )

        blacklist_token(
            jti,
            ttl
        )

        return Response(
            {"detail": "Logged out successfully"}
        )