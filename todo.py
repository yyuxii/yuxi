#!/usr/bin/env python3
"""
todo — a minimal CLI task manager
usage: python todo.py [add|done|list|clear] [task]
"""

import json
import sys
import os
from datetime import datetime

DATA_FILE = os.path.expanduser("~/.todo_data.json")


def load():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)


def save(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add(text):
    tasks = load()
    task = {
        "id": len(tasks) + 1,
        "text": text,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save(tasks)
    print(f"added: {text}")


def done(task_id):
    tasks = load()
    for t in tasks:
        if t["id"] == int(task_id):
            t["done"] = True
            save(tasks)
            print(f"done: {t['text']}")
            return
    print(f"task {task_id} not found")


def list_tasks():
    tasks = load()
    if not tasks:
        print("nothing to do.")
        return
    for t in tasks:
        status = "✓" if t["done"] else "·"
        print(f"  {status}  [{t['id']}] {t['text']}  ({t['created']})")


def clear_done():
    tasks = load()
    before = len(tasks)
    tasks = [t for t in tasks if not t["done"]]
    save(tasks)
    print(f"cleared {before - len(tasks)} task(s)")


def main():
    args = sys.argv[1:]
    if not args:
        list_tasks()
    elif args[0] == "add" and len(args) > 1:
        add(" ".join(args[1:]))
    elif args[0] == "done" and len(args) > 1:
        done(args[1])
    elif args[0] == "list":
        list_tasks()
    elif args[0] == "clear":
        clear_done()
    else:
        print("usage: python todo.py [add|done|list|clear] [task]")


if __name__ == "__main__":
    main()
