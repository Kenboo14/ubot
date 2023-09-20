from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "20063728"))
API_HASH = getenv("API_HASH", "5637eeb1cff492b89b15a1802ca99847")
BOT_TOKEN = getenv("BOT_TOKEN", "5688019347:AAFQHvzYSuIzXpuKUSFs-WLC6tbH2DSgtCE")
SESSION_STRING = getenv("SESSION_STRING", "BQAhIHQAgSSiQIvoataa5fULwCb4MWifWx3oTLDyIVZbvkY360slwP-mIkejsQ6h-Cdvztqzn-msDAZbrRcfaMXbhwiaD2MQRJbl5JJK42ZIMgalMXxi9UZHmjyFzbjFSh-zxy_oE7RLLmYeqQB0fOd7rhFgtQa96ogeQsM09vWDrhcI2N6ADWno9Xo99-CXPqF-qIgu0uQcDgCI-dfijauDGAdPgRWMJZj1InccqXwSxT8H20SlydwRtbi_dHh9mGRXHNozSh2CFjgprEl1gYGRfDnVW9KuF-AxIUJW2NiQweX5whdAAuH2myIPIfNu_lS_tfUfDncW_fqxkucoaxuZY9-1MwAAAABI2IMZAA")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://met:met@cluster0.zrjdoul.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1935806583").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1935806583").split()))
PREFIXES = getenv("PREFIXES", ", $ ) : ; - !").split()
OPENAI_API_KEY = getenv(
    "OPENAPI_API_KEY", ""
)
