import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    nExperiment = 1
    nTrial      = 10
    nRoll       = 5

    ## 北海道の５月の気温（14℃近辺）と沖縄の気温（25℃近辺）のデータ
    temperature_okinawa = [25.0, 25.1, 25.2, 25.3, 25.0, 25.1, 25.2, 25.3, 25.0, 25.1]
    temperature_hokkaido = [13.5, 14.2, 14.1, 14.3, 14.0, 14.2, 14.1, 14.0, 14.3, 14.2]

    print(f'Okinawa mean : {np.mean(temperature_okinawa):.2f}\tstd: {np.std(temperature_okinawa):.2f}')
    
    print(f'Hokkaido mean: {np.mean(temperature_hokkaido):.2f}\tstd: {np.std(temperature_hokkaido):.2f}')
    