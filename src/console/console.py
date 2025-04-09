import click

import presets.preset1
from midisport.command.load import PresetLoader
from midisport.instructionparser import PortMapSysexParser
from midisport.sysex.MidisportSysex import MidisportSysex
from midisport.sysex.midi import AMidiHandler

midi = AMidiHandler()


@click.group()
def main():
    """
    Cli to manage m-audio midisport 8x8 configuraton
    """
    pass

@main.command()
@click.argument('preset')
@click.argument('device_name')
def load(preset: str, device_name: str):
    """
    Load a certain preset
    """
    loader = PresetLoader.factory()
    preset = presets.preset1.get()

    device = midi.get_device(device_name)

    print(loader.execute(preset, device))

@main.command()
def showPresets():
    """
    Show available presets
    """
    print('only preset1 is available')

@main.command()
def showDevices():
    """
    Show availiable devices
    """
    midi = AMidiHandler()

    for device in midi.get_devices():
        print(device.getName())
