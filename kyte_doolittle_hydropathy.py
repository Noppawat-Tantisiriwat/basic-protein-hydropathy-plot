# -*- coding: utf-8 -*-
"""Kyte-Doolittle_hydropathy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_b7EvMItU81PDl2FsFdiFZU-aZufvx_g
"""

import numpy as np
import matplotlib.pyplot as plt

"""
amino_hydropathy ={"Ala":  1.800,  

"Arg": -4.500,  

"Asn": -3.500,  

"Asp": -3.500,  

"Cys":  2.500,  

"Gln": -3.500,  

"Glu": -3.500,  

"Gly": -0.400,  

"His": -3.200,  

"Ile":  4.500,  

"Leu":  3.800,  

"Lys": -3.900,  

"Met":  1.900,  

"Phe":  2.800,  

"Pro": -1.600,  

"Ser": -0.800,  

"Thr": -0.700,  

"Trp": -0.900,  

"Tyr": -1.300,  

"Val":  4.200  

}
"""

amino_hydropathy ={"A":  1.800,  

"R": -4.500,  

"N": -3.500,  

"D": -3.500,  

"C":  2.500,  

"Q": -3.500,  

"E": -3.500,  

"G": -0.400,  

"H": -3.200,  

"I":  4.500,  

"L":  3.800,  

"K": -3.900,  

"M":  1.900,  

"F":  2.800,  

"P": -1.600,  

"S": -0.800,  

"T": -0.700,  

"W": -0.900,  

"Y": -1.300,  

"V":  4.200  

}

def h_score(seq_one_letter):
  plot_val = np.array([])
  for amino in seq_one_letter:
    h_val = np.array([amino_hydropathy[amino]])
    plot_val = np.append(plot_val, h_val )
  return plot_val

# Insert sequences of amino acid
prion = "MANLGCWMLVLFVATWSDLGLCKKRPKPGGWNTGGSRYPGQGSPGGNRYPPQGGGGWGQPHGGGWGQPHGGGWGQPHGGGWGQPHGGGWGQGGGTHSQWNKPSKPKTNMKHMAGAAAAGAVVGGLGGYMLGSAMSRPIIHFGSDYEDRYYRENMHRYPNQVYYRPMDEYSNQNNFVHDCVNITIKQHTVTTTTKGENFTETDVKMMERVVEQMCITQYERESQAYYQRGSSMVLFSSPPVILLISFLIFLIVG"

print(h_score(prion))

plt.plot(np.arange(1,h_score(prion).size +1), h_score(prion))
plt.show()

def read_window_avg(scored, window):
  seq_size = scored.size
  margin = (window - 1) / 2
  start_midframe = margin + 1
  stop_midframe = (seq_size - margin) + 1
  read_area = np.arange(start_midframe, stop_midframe)
  windowed_score = np.array([])
  for frame in read_area:
    frame_start = int(frame - margin + 1)
    frame_stop = int(frame + margin + 1)
    frame_average = np.average(scored[frame_start:frame_stop])
    windowed_score = np.append(windowed_score,frame_average)

  return windowed_score

win_3_prion = read_window_avg(h_score(prion), 3) 
plt.plot(np.arange(1,win_3_prion.size + 1),win_3_prion)
plt.show()

win_5_prion = read_window_avg(h_score(prion), 5) 
plt.plot(np.arange(1,win_5_prion.size + 1),win_5_prion)
plt.show()

win_7_prion = read_window_avg(h_score(prion), 7) 
plt.plot(np.arange(1,win_7_prion.size + 1),win_7_prion)
plt.show()

win_9_prion = read_window_avg(h_score(prion), 9) 
plt.plot(np.arange(1,win_9_prion.size + 1),win_9_prion)
plt.show()

win_11_prion = read_window_avg(h_score(prion), 11) 
plt.plot(np.arange(1,win_11_prion.size + 1),win_11_prion)
plt.show()

win_13_prion = read_window_avg(h_score(prion), 13) 
plt.plot(np.arange(1,win_13_prion.size + 1),win_13_prion)
plt.show()

win_15_prion = read_window_avg(h_score(prion), 15) 
plt.plot(np.arange(1,win_15_prion.size + 1),win_15_prion)
plt.show()

win_17_prion = read_window_avg(h_score(prion), 17) 
plt.plot(np.arange(1,win_17_prion.size + 1),win_17_prion)
plt.show()

win_19_prion = read_window_avg(h_score(prion), 19) 
plt.plot(np.arange(1,win_19_prion.size + 1),win_19_prion)
plt.show()

win_21_prion = read_window_avg(h_score(prion), 21) 
plt.plot(np.arange(1,win_21_prion.size + 1),win_21_prion)
plt.show()