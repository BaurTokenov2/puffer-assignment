import os
import json
from web3 import Web3

ENV_INFURA_API_KEY="INFURA_API_KEY"
PUFFER_CONTRACT_ADDRESS = "0xD9A442856C234a39a81a089C06451EBAa4306a72"

class PufferWeb3Client:
  def __init__(self):
    self.api_key = os.getenv(ENV_INFURA_API_KEY)
    self.base_url = f"https://mainnet.infura.io/v3/{self.api_key}"
    self.w3 = Web3(Web3.HTTPProvider(self.base_url))
    self.token_contract = self.w3.eth.contract(
      address=PUFFER_CONTRACT_ADDRESS,
      abi=PufferWeb3Client.get_abi()
    )
    
  
  def get_abi():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, '../constants', 'puffer_abi.json')
    abi = json.load(open(json_url))
    return abi

  
  def get_total_supply(self):
    result = self.token_contract.functions.totalSupply().call()
    return result
  
  def get_total_assets(self):
    result = self.token_contract.functions.totalAssets().call();
    return result
  
  def get_conversion_rate(self):
    return self.get_total_assets() / self.get_total_supply();

    

  
  

  



 


