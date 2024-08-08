import numpy as np
import matplotlib.pyplot as plt

def draw_hist():
    # 20~24歳の日本人グループBの身長のデータ
    average = 170.5
    std_deviation = 5.9
    height_data = np.linspace(150, 190, 1000)
    height_dist = 1 / (std_deviation * np.sqrt(2 *np.pi)) * np.exp(-(height_data - average)**2 / (2 *std_deviation**2))
    
    plt.plot(height_data, height_dist, color='r')
    plt.title("Height Distribution of Japanese Men(20-24 years old)")
    plt.xlabel("Height (cm)")
    plt.ylabel("Probability Density")
    
    plt.grid()
    
    plt.show()

if __name__ == '__main__':
    draw_hist()
