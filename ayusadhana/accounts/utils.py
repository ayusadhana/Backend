import datetime
import random
import uuid
import pytz
import requests
from dotenv import load_dotenv
from jwt import ExpiredSignatureError, encode, decode
from rest_framework.authentication import get_authorization_header

# load_dotenv()


def generate_otp():
    ts = datetime.datetime.now(tz=pytz.UTC)
    return random.randint(100000, 999999), ts


def otp_sender(number, otp):
    api_key = "3bf58d9f-0e91-11ee-addf-0200cd936042"
    phone_number = f'+{number}'

    url = f'https://2factor.in/API/V1/{api_key}/SMS/{phone_number}/{otp}/FreskoOTP'
    requests.get(url)


def create_access_token(user_id, phone_number, role) -> str:
    data = {
        "id": str(user_id),
        "phone_number": phone_number,
        "role": role
    }
    expire_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=5)
    token_payload = {
        "data": data,
        "exp": expire_time,
        "iat": datetime.datetime.now(datetime.UTC)
    }
    secret = "access secret"
    try:
        access_token = encode(token_payload, secret, algorithm="HS256")
        return access_token
    except Exception as e:
        raise ValueError("Unable to create access token") from e


def decode_access_token(token) -> dict:
    try:
        payload = decode(token, "access secret", algorithms="HS256")
        payload["data"]["id"] = uuid.UUID(payload["data"]["id"])
        return payload["data"]

    except ExpiredSignatureError:
        raise ValueError("Token has expired")

    except Exception as e:
        raise ValueError("Unable to decode access token") from e


def authorize_user(request) -> dict:
    header_auth = get_authorization_header(request).split()
    if header_auth and len(header_auth) == 2:
        token = header_auth[1].decode("utf-8")
        data = decode_access_token(token)

        if data:
            return data
    raise ValueError("Unauthorized")
