
from signalz import ecgsyn
import paper_ecg
import numpy as np
import time
import math

duration = 10
hrmean = 60.
hrstd = 1
sfecg = 100
sfint = 100
n = math.ceil(hrmean*duration/60)
rhythm_lead = 1

def generate_ecg_values(values):
    signals = []
    rhythm_signal = []
    for lead in range(0,12):
        y = ecgsyn(**values[lead])[0][:math.ceil(sfecg*duration)]# is there room for performance imporvements here? We seem to generate more ekg than we use
        signals.append(y)

    signals_arr = np.array(signals)
    
    return signals_arr

def generate_ecg_plot(signals_arr,title):
    plot(signals_arr, sample_rate=sfecg, title=title)
    save_as_svg("test_svg")

test_values_lead = {"sfecg" : sfecg,
    "n" : n,
    "hrmean" : hrmean,
    "hrstd" : hrstd,
    "lfhfratio" : 0.5,
    "sfint" : sfint,
    "ti" : [-70, -15, 0, 15, 100],
    "ai" : [1.2, -5, 30, -7.5, 0.75],
    "bi" : [0.25, 0.1, 0.1, 0.1, 0.4]
}

test_values = {lead: test_values_lead for lead in range(0,12)}
t0 = time.time()

signal = generate_ecg_values(test_values)
paper_ecg.plot(signal,sample_rate=sfecg,title="Georgey")
paper_ecg.save_as_svg("test_svg")
t1 = time.time()

print(t1-t0)


