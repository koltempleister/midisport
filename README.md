# midisport preset manager

### Status

[![Python application](https://github.com/koltempleister/midisport/actions/workflows/python-app.yml/badge.svg)](https://github.com/koltempleister/midisport/actions/workflows/python-app.yml)

settings editor for m-audio midisport 8x8

still under development

## cli commands
list all possible presets
```bash
python src/console/console.py showPresets
```
show possible devices (midisport isnt detected automatically yet)
```bash
python src/console/console.py showDevices
```
load preset onto device
```bash
python src/console/console.py load <preset> <device-name>
```

## troubleshooting

### how to get mido working with alsa?

make sure libasound2-dev is installed

```bash
sudo apt install libasound2-dev
```
