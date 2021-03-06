import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt

def dist_inds(L1,Pathx,Pathy,ACStatex,ACStatey,ACStatez,ACStatechi):
	PX = np.array(Pathx)
	PY = np.array(Pathy)
	Dists = np.sqrt((PX-ACStatex)**2 + (PY-ACStatey)**2)
	dist_sort = np.argsort(np.absolute(L1-Dists))
	return dist_sort
