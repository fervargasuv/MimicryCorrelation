from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest
from scipy.stats import shapiro
from scipy.stats import jarque_bera
from scipy.stats import anderson

class MimicryProcessor:

    def __init__(self):
        pass
        
    def cal_dur_mim(self,matriz_x_1,matriz_y_1,matriz_x_2,matriz_y_2):
        # Calcula la duración de cada caso de mimetismo.    
        correlacionx=[]
        correlaciony=[]
        correlaciont=[]
        for i in range(0,49):
            correlationx = np.corrcoef(matriz_x_1[i], matriz_x_2[i])[0, 1]
            correlationy=np.corrcoef(matriz_y_1[i], matriz_y_2[i])[0, 1]
            correlacionx.append(correlationx)
            correlaciony.append(correlationy)
        
        for i in range(0,49):
            r_total = sqrt(float(correlacionx[i])**2 + float(correlaciony[i])**2)
            correlaciont.append(r_total)

        print(correlaciont)

        return correlaciont


    