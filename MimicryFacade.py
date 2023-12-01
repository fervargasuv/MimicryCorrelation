

import MimicryProcessor
import MimicryDataReader


class MimicryFacade:
    def __init__(self):
        self.data_reader = MimicryDataReader.MimicryDataReader()
        self.processor = MimicryProcessor.MimicryProcessor()

    def process_data(self, datos):
        datos = self.data_reader.read_data_csv(datos)
        matriz_x_1,matriz_y_1=self.data_reader.read_data_frames(datos[0]["participante_1"])
        matriz_x_2,matriz_y_2=self.data_reader.read_data_frames(datos[0]["participante_2"])
        matriz_mim_x_1,matriz_mim_y_1=self.data_reader.mimicry_frames(matriz_x_1,matriz_y_1,datos[0]["frame_inicio"],datos[0]["frame_fin"])
        matriz_mim_x_2,matriz_mim_y_2=self.data_reader.mimicry_frames(matriz_x_2,matriz_y_2,datos[0]["frame_inicio"],datos[0]["frame_fin"])

        return self.processor.cal_dur_mim(matriz_mim_x_1,matriz_mim_y_1,matriz_mim_x_2,matriz_mim_y_2)