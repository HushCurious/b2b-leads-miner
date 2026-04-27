#!/usr/bin/env python3
"""Resolve default vs user-defined output config files for b2b-leads-miner."""

from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "assets" / "output-config"


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


def choose(default_name: str, user_name: str) -> dict:
    default_path = CONFIG_DIR / default_name
    user_path = CONFIG_DIR / user_name
    user_value = read_text(user_path)
    chosen = user_path if user_value else default_path
    return {
        "default_file": str(default_path),
        "user_file": str(user_path),
        "selected_file": str(chosen),
        "selected_value": read_text(chosen),
    }


def user_only(name: str) -> dict:
    path = CONFIG_DIR / name
    value = read_text(path)
    return {
        "user_file": str(path),
        "selected_file": str(path) if value else "",
        "selected_value": value,
    }


def main() -> None:
    result = {
        "columns": choose("file_columns.md", "file_columns_userDefine.md"),
        "format": choose("file_format.md", "file_format_userDefine.md"),
        "filepath": user_only("filepath_userDefine.md"),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
