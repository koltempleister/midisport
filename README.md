# midisport preset manager

### Status

[![Python package](https://github.com/koltempleister/midisport/actions/workflows/python-package.yml/badge.svg)](https://github.com/koltempleister/midisport/actions/workflows/python-package.yml)

settings editor for m-audio midisport 8x8

still under development

## cli commands

```bash
python src/console/console.py showPresets
```

```bash
python src/console/console.py showDevices
```

```bash
python src/console/console.py load <preset> <device-name>
```

## troubleshooting

### how to get mido working with alsa?

make sure libasound2-dev is installed

```bash
sudo apt install libasound2-dev
```
