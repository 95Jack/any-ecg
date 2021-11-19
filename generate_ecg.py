from signalz.generators import ecgsyn
import numpy as np

def generate_ecg(values, text):
    signals = []
    for lead in range(1,12):
        x = ecgsyn(**values[lead])
        signals.append(x)
    signals_arr = np.array(signals)
    print(signals_arr.length)

test_values_lead = {"sfecg" : 256,
    "n" : 256,
    "hrmean" : 60.,
    "hrstd" : 1,
    "lfhfratio" : 0.5,
    "sfint" : 512,
    "ti" : [-70, -15, 0, 15, 100],
    "ai" : [1.2, -5, 30, -7.5, 0.75],
    "bi" : [0.25, 0.1, 0.1, 0.1, 0.4]
}

test_values = {lead: test_values_lead for lead in range(1,12)}

generate_ecg(test_values, "Georgey")



