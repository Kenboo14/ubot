from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "20063728"))
API_HASH = getenv("API_HASH", "5637eeb1cff492b89b15a1802ca99847")
BOT_TOKEN = getenv("BOT_TOKEN", "6263702391:AAGXOIwMEN-I3aa9PBtvIQcli78Zer9oFEo")
SESSION_STRING = getenv("SESSION_STRING", "BQFYfdEAJtvExhPSvh-KdufLqB6O2PajdcJMYPtvk1EnsrdaA5mj-sCqI-VjGPv9AydUCPo9MyFRJMzSnxW7mUSBGAsnRRzMgi1FaWVD0cp_HTFr_Gph4i9d0m5twfM2JpS2oEGmDZL7_eWpE2wRBiuhz34A9zhz6x3uHCgaGi2ctGjr1BMCgDjEETUD1mqzjqEYywnwoDCXqib8EbtoMhdwH59yXZ1xNueW2IvwRirwJfIdxpGwRvqrIWcY_9m3UjMbozbBPhyTthWOBarJKE_mVs7YZvmA45_E9dkg6XjTkGkKlgqLVFTdcy11TfqQjN8dZ8uybg77-MQCMvEF3S1pEsJrEAAAAABzYhB3AA")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://met:met@cluster0.zrjdoul.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1935806583").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1935806583").split()))
PREFIXES = getenv("PREFIXES", ", $ ) : ; - !").split()
OPENAI_API_KEY = getenv(
    "OPENAPI_API_KEY", ""
)
