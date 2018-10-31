import requests
import uuid
from random import choice


BASE_URL = "https://www.appburgerking.cl"
HEADERS = {
    'Origin': "https://www.appburgerking.cl",
    'X-Requested-With': "XMLHttpRequest",
    'Referer': "https://www.appburgerking.cl/",
}

NAMES = [
    "Hugo",
    "Sebastian",
    "Victor",
    "Santiago",
    "Jose",
    "Alex",
    "Andres",
    "Rodrigo",
    "Felipe",
    "Pablo",
    "Cristian",
    "Michael",
    "Daniel",
    "David",
    "Eduardo"
]

LAST_NAMES = [
    "Castañeda",
    "Rojas",
    "Urrutia",
    "Ruiz",
    "Bello",
    "Santander",
    "Salazar",
    "Palacio",
    "Soto",
    "Cortes",
    "Tapia",
    "Perez",
    "Pavez",
    "Romero",
    "Castro",
    "Zambrano"
]


def register(email, password):
    path = "/auth/register"

    payload = {
        "firstName": choice(NAMES),
        "gender": "male",
        "lastName": choice(LAST_NAMES),
        "birthday-d": 1,
        "birthday-m": 1,
        "birthday-y": 1985,
        "birthday": "1985-01-01",
        "email": email,
        "pass": password,
    }
    response = requests.post(BASE_URL + path, data=payload, headers=HEADERS).json()
    return response["status"] == "ok"


def login(email, password):
    path = "/auth/login"

    payload = {
        "email": email,
        "pass": password
    }
    response = requests.post(BASE_URL + path, data=payload, headers=HEADERS).json()
    if response["status"] != "ok":
        return None

    return response["payload"]["user"]["id"]


def activate_coupon(uid, cid):
    path = "/coupon/activation"

    payload = {
        "couponId": cid,
        "userId": uid,
        "skey": str(uuid.uuid4())
    }
    response = requests.post(BASE_URL + path, data=payload, headers=HEADERS).json()

    if response["status"] != "ok":
        return None
    return response["payload"]["activationId"]


def get_coupon_qr(aid):
    path = "/coupon/qr/{}/json".format(aid)

    response = requests.get(BASE_URL + path, headers=HEADERS).json()
    if response["status"] != "ok":
        return None
    return response["payload"]["qrcode"]


def get_coupon_image(aid):
    path = "/coupon/qr/{}".format(aid)

    return requests.get(BASE_URL + path, headers=HEADERS, stream=True).raw
