#!/usr/bin/env python3
"""Create local venv, install dependencies, migrate DB, and run server."""
from pathlib import Path
import subprocess
import sys


def run(cmd, cwd=None):
    return subprocess.run(cmd, cwd=cwd, check=False)


def main():
    repo_root = Path(__file__).resolve().parent
    project_root = repo_root / "ecommerce-master"
    requirements = project_root / "requirement.txt"
    venv_root = repo_root / ".venv"
    venv_python = venv_root / "Scripts" / "python.exe"

    if not project_root.exists():
        print(f"ERROR: Project directory not found: {project_root}")
        return 1
    if not requirements.exists():
        print(f"ERROR: Requirements file not found: {requirements}")
        return 1

    print(f"Using base Python: {sys.executable}")
    print(f"Project root: {project_root}")

    if not venv_python.exists():
        print("Creating virtual environment...")
        rc = run([sys.executable, "-m", "venv", str(venv_root)])
        if rc.returncode != 0:
            return rc.returncode
    else:
        print("Using existing virtual environment.")

    print("Installing dependencies...")
    rc = run([str(venv_python), "-m", "pip", "install", "--upgrade", "pip"])
    if rc.returncode != 0:
        return rc.returncode
    rc = run([str(venv_python), "-m", "pip", "install", "-r", str(requirements)])
    if rc.returncode != 0:
        return rc.returncode

    print("Running migrations...")
    rc = run([str(venv_python), "manage.py", "migrate", "--noinput"], cwd=str(project_root))
    if rc.returncode != 0:
        return rc.returncode

    print("Starting server at http://127.0.0.1:8000")
    rc = run([str(venv_python), "run_server.py"], cwd=str(project_root))
    return rc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
