# todo-cli

minimal task manager for the terminal. no dependencies, no setup, just python.

## usage

```bash
python todo.py              # list tasks
python todo.py add fix bug  # add a task
python todo.py done 1       # mark task 1 as done
python todo.py clear        # remove completed tasks
```

## example

```
$ python todo.py add write unit tests
added: write unit tests

$ python todo.py add fix login bug
added: fix login bug

$ python todo.py list
  ·  [1] write unit tests  (2024-03-12 10:32)
  ·  [2] fix login bug      (2024-03-12 10:33)

$ python todo.py done 2
done: fix login bug

$ python todo.py list
  ·  [1] write unit tests  (2024-03-12 10:32)
  ✓  [2] fix login bug      (2024-03-12 10:33)
```

tasks are saved in `~/.todo_data.json`.
