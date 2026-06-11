from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

from apps.accounts.services.token_blacklist import (
    is_token_blacklisted
)


class BlacklistJWTAuthentication(
    JWTAuthentication
):
    def get_validated_token(
        self,
        raw_token
    ):

        token = super().get_validated_token(
            raw_token
        )

        jti = token.get("jti")

        if is_token_blacklisted(jti):
            raise AuthenticationFailed(
                "Token has been revoked."
            )

        return token