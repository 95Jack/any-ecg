
from signalz import ecgsyn
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

def generate_ecg(values, text):
    signals = []
    rhythm_signal = []
    for lead in range(0,12):
        y = ecgsyn(**values[lead])[0][:math.ceil(sfecg*duration)]
        signals.append(y)

    signals_arr = np.array(signals)
    
    print(signals_arr.shape)
    print(rhythm_signal)

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

generate_ecg(test_values, "Georgey")
t1 = time.time()

print(t1-t0)


