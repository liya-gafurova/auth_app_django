Token Auth

# Using [Djoser](https://github.com/sunscrapers/djoser) Auth Library

[Available endpoints](https://djoser.readthedocs.io/en/latest/getting_started.html)

Suitable for token auth: 
 - token (uses  'rest_framework.authtoken' from DRF for token storing)
 - JWT token
 - Social auth 
 - user data management works with custom user model (including registration) 

# Using [dj-rest-auth](https://github.com/jazzband/dj-rest-auth) Auth library (current fork of [django-rest-auth](https://github.com/Tivix/django-rest-auth))

- token
- User registration
- Social auth
- JWT token

Subjectively, **dj-rest-auth** is more convenient because it does not have an extra number of endpoints, which are in djoser (*users/*)