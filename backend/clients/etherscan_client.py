import os
import requests

ENV_ETHERSCAN_API_KEY = "ETHERSCAN_API_KEY"

class EtherscanClient:
  def __init__(self): 
    self.api_key = os.getenv(ENV_ETHERSCAN_API_KEY)
    self.base_url = "https://api.etherscan.io/api"


  def get_total_supply(self, contract_address):
    url = f"{self.base_url}?module=stats&action=tokensupply&contractaddress={contract_address}&apikey={self.api_key}"
    response = requests.get(url)
    data = response.json()
    return data['result']
  
  def get_contract_abi(self, contract_address):
    url = f"{self.base_url}?module=contract&action=getabi&address={contract_address}&apikey={self.api_key}"
    response = requests.get(url)
    data = response.json()
    return data['result']
  
 
