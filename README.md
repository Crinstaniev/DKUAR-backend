# DKUAR Backend

This is the backend for DKUAR project. This project is under active development

## Installation and Deployment

### Create virtual environment

Use `venv` to create virtual environment and activate

```shell
python3 -m venv ./venv
. venv/bin/activate
```

Install dependencies

```shell
pip install -r requirements.txt
```

Run the backend (in production mode or dev mode)
```shell
make prod # in production mode
make dev  # in dev mode
```

### API available

[dummy/fetch](doc/fetch.md)

## Roadmap

- [X] Dummy backend
- [ ] Docker-compose deployment
- [ ] (Temporary) YOLOv5 for object detection
- [ ] Model optimization
