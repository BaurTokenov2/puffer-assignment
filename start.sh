#!/bin/bash

source backend/venv/bin/activate

# start backend
(cd backend && pip install -r requirements.txt && python app.py) & 

# start frontend
(cd frontend && npm install && npm run dev)