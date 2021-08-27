from dotenv import load_dotenv
load_dotenv()
from python_kroger_client.python_kroger_client import config
from python_kroger_client.python_kroger_client.client import KrogerServiceClient




print("==================================================")
print("============== SERVICE CLIENT ====================")
print("==================================================")
service_client = KrogerServiceClient(encoded_client_token=config.encoded_client_token)
products = service_client.search_products(term="Taco", limit=10, location_id='02600845')
print()
print("PRODUCTS")
print("==================================================")
print()
for p in products: print(p)
print()