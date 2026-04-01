#!/usr/bin/env python
import os
import sys
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parent
    project_root = repo_root / "ecommerce-master"

    if not project_root.exists():
        print(f"ERROR: Project directory not found: {project_root}")
        return 1

    os.chdir(project_root)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        print("ERROR: Django is not installed in the active Python environment.")
        print("Run setup_and_run.py first, then retry.")
        return 1

    execute_from_command_line(["manage.py", "runserver", "127.0.0.1:8000"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
