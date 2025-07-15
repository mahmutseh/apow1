# To-Do App

This repository contains a simple to-do list application with a graphical user interface built using Python's `tkinter` library. The program works on Windows 10 and other platforms where Python is available.

## Requirements

* Python 3.7 or later (includes `tkinter`)

## Usage

Run the application with:

```bash
python todo_gui.py
```

A window will open allowing you to add tasks to your list and delete them when finished.

## Binance Futures Alert Web App (Prototype)

This repository also contains a basic prototype for a Binance Futures alert system.
It consists of a **FastAPI** backend and a **React** frontend using Material UI.
The goal is to stream real-time price updates from Binance via WebSocket and
provide a modern web interface with alarm functionality.

### Quick start

1. Run the setup script (creates Python virtual environment and installs
   dependencies). If `npm` is installed it will also install frontend packages:

   ```bash
   ./setup.sh
   ```

2. Start the backend API:

   ```bash
   .venv/bin/uvicorn backend.main:app --reload
   ```

3. In another terminal start the React development server:

   ```bash
   cd frontend
   npm start
   ```

The React app will connect to the backend WebSocket at `ws://localhost:8000/ws`
and display incoming trade messages.

This is a starting point. Further work is required to implement alarm settings,
CSV export, multiple user preferences, and a polished interface.

