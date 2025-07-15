import os
import sys
import subprocess
import shutil
from pathlib import Path


def run_cmd(cmd, cwd=None):
    """Run a subprocess command and exit on failure."""
    try:
        print("Running:", " ".join(cmd))
        subprocess.run(cmd, cwd=cwd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command '{' '.join(cmd)}' failed with exit code {e.returncode}")
        sys.exit(e.returncode)


def main():
    root = Path(__file__).resolve().parent
    venv_dir = root / '.venv'

    if os.name == 'nt':
        bin_dir = venv_dir / 'Scripts'
        python_exec = bin_dir / 'python.exe'
        pip_exec = bin_dir / 'pip.exe'
    else:
        bin_dir = venv_dir / 'bin'
        python_exec = bin_dir / 'python'
        pip_exec = bin_dir / 'pip'

    if not venv_dir.exists():
        print('Creating virtual environment...')
        run_cmd([sys.executable, '-m', 'venv', str(venv_dir)])

    print('Installing backend dependencies...')
    run_cmd([str(pip_exec), 'install', '-r', str(root / 'backend/requirements.txt')])

    npm = shutil.which('npm')
    if npm:
        node_modules = root / 'frontend' / 'node_modules'
        if not node_modules.exists():
            print('Installing frontend dependencies...')
            run_cmd([npm, 'install'], cwd=root / 'frontend')
    else:
        print('npm not found. Please install Node.js to run the frontend.')

    print('Starting backend and frontend... (Press Ctrl+C to stop)')
    backend_proc = subprocess.Popen([str(python_exec), '-m', 'uvicorn', 'backend.main:app', '--reload'])
    frontend_proc = None
    if npm:
        frontend_proc = subprocess.Popen([npm, 'start'], cwd=root / 'frontend')

    try:
        backend_proc.wait()
    except KeyboardInterrupt:
        print('Shutting down...')
    finally:
        if frontend_proc:
            frontend_proc.terminate()
        backend_proc.terminate()


if __name__ == '__main__':
    main()
