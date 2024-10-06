from flask import Flask, jsonify
from dotenv import load_dotenv
from clients import puffer_web3_client
from flask_cors import CORS

# environment setup
load_dotenv()

def create_app():
  app = Flask(__name__)
  CORS(app)
  puffer_client = puffer_web3_client.PufferWeb3Client()

  @app.route('/conversion_rate')
  def conversion_rate():
    return jsonify({
      'data': puffer_client.get_conversion_rate()
    })

  return app 

if __name__ == "__main__":
  app = create_app()
  app.run(debug=True)

