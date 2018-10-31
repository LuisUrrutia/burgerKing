import os
from burger import register, login, activate_coupon, get_coupon_qr

BASE_EMAIL = os.getenv("BK_USER", "temp")
BASE_DOMAIN = os.getenv("BK_DOMAIN", "yopmail.com")
DEFAULT_PASSWORD = os.getenv("BK_PASS", "123456")
COUPON = os.getenv("BK_COUPON", "5bce1252472700001a04b2e2")
FROM = os.getenv("BK_FROM", 1);
TO = os.getenv("BK_TO", 10);

for x in range(int(FROM), int(TO)):
    eid = '{0:03d}'.format(x)
    email = "{}{}@{}".format(BASE_EMAIL, eid, BASE_DOMAIN)

    result = register(email, DEFAULT_PASSWORD)
    if not result:
        print("[-] E-Mail couldn't be registered: {}".format(email))
        continue

    input("Registered E-Mail: {}".format(email))

    uid = login(email, DEFAULT_PASSWORD)
    if uid is None:
        print("[-] Can't login with E-Mail: {}".format(email))
        continue

    aid = activate_coupon(uid, COUPON)
    if aid is None:
        print("[-] Couldn't activate the coupon for the account: {}".format(email))
        continue

    qr = get_coupon_qr(aid)
    if qr is None:
        print("[-] QR couldn't be obtained for the account: {}".format(email))

    print("[+] QR of the account {} is: {} and Hash: {}".format(email, qr, aid))
