#!/bin/bash

set -e

# Create Python venv and install backend deps
python3 -m venv .venv
. .venv/bin/activate
pip install -r backend/requirements.txt

deactivate

# Install frontend deps if npm is available
if command -v npm >/dev/null 2>&1; then
  cd frontend && npm install && cd ..
else
  echo "npm not found. Please install Node.js and run 'npm install' in the frontend directory." >&2
fi

echo "Setup complete. Run backend with:"
echo "  .venv/bin/uvicorn backend.main:app --reload" 
echo "and in another terminal start the React dev server with 'npm start' inside frontend." 
