
import numpy as np
from numpy import newaxis
import keras
from keras.models import Sequential
from keras.layers import Activation, Dropout, Flatten, Dense, LSTM, TimeDistributed
import pandas as pd
import h5py

def init():
    global trainedmod
    from keras.models import load_model
    
    trainedmod = load_model("finalmodel.sav")
def run(npa):
    global trainedmod
    
    if (len(npa.shape) > 1):
        ypred = trainedmod.predict(npa.reshape(npa.shape[0],24,1))
    else:
        ypred = trainedmod.predict(npa.reshape(1,24,1))
    retdf = pd.DataFrame(data={"Scored Values":np.squeeze(np.reshape(ypred, newshape= [-1,1]), axis=1)})
    return str(retdf)
if __name__ =="__main__":
    init()
    tmpX = np.array([[   4.50000000e+02,   3.53000000e+02,   2.85000000e+02,   3.32000000e+02,
                3.77000000e+02,   2.68000000e+02,   2.18000000e+02,   3.87000000e+02,
                8.34000000e+02,   5.08000000e+02,   1.53000000e+02,   4.20000000e+01,
                4.00000000e+00,   1.00000000e+00,   1.00000000e+01,   1.70000000e+01,
                0.00000000e+00,   4.00000000e+00,   1.00000000e+00,   2.00000000e+00,
                5.80000000e-01,   5.45500000e-01,   6.40000000e-01,   3.28400000e-01],
            [   8.90000000e+02,   4.50000000e+02,   3.53000000e+02,   2.85000000e+02,
                3.32000000e+02,   3.77000000e+02,   2.68000000e+02,   2.18000000e+02,
                3.87000000e+02,   8.34000000e+02,   5.08000000e+02,   1.53000000e+02,
                4.00000000e+00,   1.00000000e+00,   1.00000000e+01,   1.80000000e+01,
                0.00000000e+00,   4.00000000e+00,   1.00000000e+00,   2.00000000e+00,
                5.60000000e-01,   5.30300000e-01,   6.40000000e-01,   3.28400000e-01]])
    
    predY = run(tmpX[0:2,:])
    print(predY)