#Importing the Libraries
from dotenv import load_dotenv
import os

#Loading the Environment Variables
load_dotenv()
api_key = os.getenv("API_KEY")

#Validating
print(f'API_KEY present:{bool(api_key)}')