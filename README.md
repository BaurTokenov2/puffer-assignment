## Puffer Conversion Rate assignment

### Prerequisites
#### 1.Setting up an API key to set-up blockchain connection
- Sign up and obtain developer API key on https://app.infura.io/register
- Run the following command from this project's root to create a .env file in the backend folder with your api_key
  - `echo INFURA_API_KEY="<YOUR_INFURA_API_KEY>" > backend/.env`
  - it should have created a file in ./backend/.env with your INFURA_API_KEY which will be needed for the Web3Client to connect to the blockchain.

#### 2. Make sure you have the following installed
- Python 3.8.10
- Node v18.11.0

### How to start the servers

1. Give access to the start.sh script via `chmod +x start.sh`
2. Run `./start.sh` in the command line
3. You should now have a React app running on http://127.0.0.1:5173/ which is polling data from http://127.0.0.1:5000/conversion_rate