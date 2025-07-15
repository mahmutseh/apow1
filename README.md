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

Run the helper script `start.py` to set everything up and launch both the
backend and frontend in one step. It creates a virtual environment, installs all
dependencies and then starts the servers. The script works on Windows and
Unix-like systems. Press `Ctrl+C` to stop them.

```bash
python start.py
```

The React app will connect to the backend WebSocket at `ws://localhost:8000/ws`
and display incoming trade messages.

This is a starting point. Further work is required to implement alarm settings,
CSV export, multiple user preferences, and a polished interface.

