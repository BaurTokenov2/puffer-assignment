from flask import Flask
from dotenv import load_dotenv
from clients import etherscan

# environment setup
load_dotenv();
PUFFER_CONTRACT_ADDRESS = "0xD9A442856C234a39a81a089C06451EBAa4306a72"


def create_app():
  app = Flask(__name__)
  etherscan_client = etherscan.EtherscanClient();

  @app.route('/')
  def hello_world():
    return etherscan_client.get_total_supply(PUFFER_CONTRACT_ADDRESS)

  return app 

if __name__ == "__main__":
  app = create_app();
  app.run(debug=True)

