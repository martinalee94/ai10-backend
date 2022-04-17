import random

import jwt
from config.settings.base import SIMPLE_JWT
from django.core.exceptions import ObjectDoesNotExist
from faker import Faker


def get_calories(weight, duration):
    # 식 : MET(요가 에너지소비량) x Weight(몸무게)  x 0.0175 x Time(min) = Kcal
    return round(3.1 * weight * 0.0175 * duration / 60)


def get_decoded_token(token):
    options = {
        "verify_signature": False,
        "verify_aud": False,
        "require_sub": True,
    }
    decoded_token = jwt.decode(
        token,
        SIMPLE_JWT["SIGNING_KEY"],
        algorithms=[SIMPLE_JWT["ALGORITHM"]],
        options=options,
    )
    return decoded_token


nickname_pool = []


def get_nickname():
    from data.load_nickname import load_nickname

    from apps.users.models import User

    global nickname_pool

    if nickname_pool == []:
        nickname_pool = load_nickname()
    while True:
        nickname = nickname_pool[random.randrange(0, len(nickname_pool), 1)]
        try:
            User.objects.get(nickname=nickname)
        except ObjectDoesNotExist:
            return nickname
