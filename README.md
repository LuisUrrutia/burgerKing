# Burger King Coupon Generator

> Register an account, login, activate a coupon and generate a fake screenshot

The application [Burker King Chile](https://play.google.com/store/apps/details?id=com.crazycake.burgerkingchile) gave away coupons for a free Whopper if you registered an account.

The application didn't have and has no Terms of Services neither in the application or in the Google Play Store so I created this PoC to register accounts, activate coupons and generate fake screenshot with the coupon data.

## Getting started

Install the requirements

```
pip install -r requirements
```

Register, log in and activate coupons. Behavior can be modified with environment variables:

| Env. Variable | Description | Default |
| --- | --- | --- |
| BK_USER | Base username for the email: **temp**001@domain.com | temp |
| BK_DOMAIN | Base domain for the email: temp001@**domain.com** | yopmail.com |
| BK_PASS | Password of the account | 123456 |
| BK_COUPON | Coupon ID to activate | 5bce1252472700001a04b2e2 |
| BK_FROM | Start the username from this number: temp**001**@domain.com | 1 |
| BK_TO | End the username with this number: temp**010**@domain.com | 10 |

```
python register.py
```

Generate screenshot. You must edit this file and add your hashes to `CODES` list.

```
python generate.py
```
