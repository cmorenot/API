# import string
# import random
# Get ascii Characters numbers and punctuation (minus quote characters as they could terminate string).
# chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')
# SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(50)])
# print(SECRET_KEY)

"""Descomentar las 5 primeros lineas y comentar la linea 10....para generar SECRET_KEY automaticamente cada ves q se ejecuta el programa"""

SECRET_KEY = "abdI7>}TpFYu<aV=`HbH`SKU8xIM:H474=&e{$9jKD!:HUI6L9"

ALLOWED_HOSTS = ['*']



"""Conficuracion de la BBDD rh y int"""

DB_NAME_RH = 'OLM_RH'
DB_NAME_INT = 'OLM_INT'

DB_HOST_RH = '127.0.0.1'
DB_USER_RH = 'sa'
DB_PWD_RH = 'temporal123'
DB_PORT_RH = ''

"""Configuracion de BBDD de SIGENU"""

DB_NAME_SIGENU = 'sigenu_student'
DB_USER_SIGENU = 'postgres'
DB_PASSWORD_SIGENU = 'admin'
DB_HOST_SIGENU = '127.0.0.1'
DB_PORT_SIGENU = '5432'