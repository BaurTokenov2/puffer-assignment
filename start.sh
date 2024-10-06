#!/bin/bash

source backend/venv/bin/activate

# start backend
(cd backend && pip install -r requirements.txt && python3 app.py) & 

# start frontend
(cd frontend && npm install && npm run dev)
