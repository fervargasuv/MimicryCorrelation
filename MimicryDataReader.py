import csv
import os
import numpy as np
class MimicryDataReader:

    def __init__(self):
        pass

    def read_data_csv(self,archivos_csv):
        data = []
        for archivo_csv in archivos_csv:
            with open(archivo_csv, "r") as f:
                next(f)
                for line in f:
                    data.append({
                        "participante_1": line.split(",")[5],
                        "participante_2": line.split(",")[6],
                        "frame_inicio": int(line.split(",")[7]),
                        "frame_fin": int(line.split(",")[8])
                    })
        return data
    

    def read_data_frames(self,participante):
        matriz_x = []
        matriz_y=[]
        participante=participante.strip('"')
        ruta_carpeta = os.path.join('C:\\Users\\nekos\\OneDrive\\Documentos\\Tesis\\Codigo tesis\\Full_Videos_Frames',participante)
        print(ruta_carpeta)
        archivos = os.listdir(ruta_carpeta)
        for archivo in archivos:
            if 'Landmarks' in archivo:
                ruta_subcarpeta = os.path.join(ruta_carpeta, archivo)
                break
        subcarpeta = os.listdir(ruta_subcarpeta)
        for archivo in subcarpeta:
            if archivo.endswith('.txt'):
                with open(os.path.join(ruta_subcarpeta, archivo), 'r') as archivotxt:
                    lineas = archivotxt.readlines()

                    # Extraer coordenadas (x, y) de los 49 landmarks de la tercera línea
                    coordenadas = lineas[2].strip().split()
                    # Crear una lista de matrices para almacenar las coordenadas (x, y)
                    datos_x = []
                    datos_y=[]
                    for i in range(0, len(coordenadas), 2):
                        datos_x.append(float(coordenadas[i]))
                        datos_y.append(float(coordenadas[i+1]))
                    matriz_x.append(datos_x)
                    matriz_y.append(datos_y)


        matriz_x=np.array(matriz_x)
        matriz_y=np.array(matriz_y)

        matriz_x=matriz_x.T
        matriz_y=matriz_y.T

        return matriz_x,matriz_y

    def mimicry_frames(self,matriz_x,matriz_y,frame_inicio,frame_fin):
        matriz_mim_x = matriz_x[:, frame_inicio:frame_fin + 1]
        matriz_mim_y = matriz_y[:, frame_inicio:frame_fin + 1]

        matriz_mim_x=np.array(matriz_mim_x)
        matriz_mim_y=np.array(matriz_mim_y)

        return matriz_mim_x, matriz_mim_y

