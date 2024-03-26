from datetime import datetime, timedelta

import jwt

JWT_EXP_DATE = datetime.now() + timedelta(hours=48)  # Expires in 48 hours
JWT_SECRET_KEY = '<#123>'


def is_jwt_valid(jwt_token=None) -> bool:
    """
    Check if the JWT token is valid.

    Parameters:
        - jwt_token (str): JWT token to be validated.

    Returns:
        - bool: True if the token is valid, False otherwise.
    """
    try:
        decoded_token = jwt.decode(jwt_token, verify=False)  # Decoding without verification
        expiration_time = datetime.fromtimestamp(decoded_token['exp'])
        current_time = datetime.utcnow()
        return current_time < expiration_time
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
