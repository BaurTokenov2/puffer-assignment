from flask import Flask
from dotenv import load_dotenv
from clients import puffer_web3_client, etherscan_client

# environment setup
load_dotenv();
PUFFER_CONTRACT_ADDRESS = "0x4aa799c5dfc01ee7d790e3bf1a7c2257ce1dceff"


def create_app():
  app = Flask(__name__)
  etherscan_client_instance = etherscan_client.EtherscanClient();
  web3_client_instance = puffer_web3_client.PufferWeb3Client();

  @app.route('/')
  def hello_world():
    return f"Conversion rate:{web3_client_instance.get_conversion_rate()}"

  return app 

if __name__ == "__main__":
  app = create_app();
  app.run(debug=True)

