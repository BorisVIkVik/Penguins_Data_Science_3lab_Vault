import hvac
import sys
from dotenv import load_dotenv
import os

load_dotenv()  # Загружает .env в os.environ

# DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PSW = os.getenv('DB_PSW')

# print(VAULT_TOKEN)  # Значение из .env
client = hvac.Client(
    url='http://vault:8200',
    token='testtoken',
)


create_response = client.secrets.kv.v2.create_or_update_secret(
    path='my-secret-password',
    secret=dict(password=DB_PSW),
)

print('Secret written successfully.')

# # read_response = client.secrets.kv.read_secret_version(path='my-secret-password')

# # password = read_response['data']['data']['password']



# # if password != 'test123':
# #     sys.exit('unexpected password')

# # print('Access granted!')
