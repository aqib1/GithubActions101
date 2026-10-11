# GitHub Actions 101

A small Python project used to learn GitHub Actions, tests, and package builds.

## Run the app

```sh
uv run --locked main.py
```

## Run tests

```sh
uv run --locked python -m unittest discover -s tests -v
```

## Build the package

```sh
uv build
```

Build artifacts are written to `dist/`.
