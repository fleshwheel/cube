#!/usr/bin/env python3

import click
import numpy as np

import sounddevice as sd

sd.default.samplerate = 192000
sd.default.device = "AG06/AG03"
sd.default.latency = "low"

from scipy.io.wavfile import read, write

@click.command()
@click.argument("in_file", required=True)
@click.argument("out_file", required=True)
@click.option("-r", "--sample-rate", default=192000, help="Sample rate for record reservoir response.")
def apply(in_file, out_file, sample_rate):

    rate, data = read(in_file)
    
    recording = sd.playrec(data, sample_rate, dtype="float64", channels=2, blocking=True)

    write(out_file, sample_rate, recording)

if __name__ == "__main__":
    apply()
