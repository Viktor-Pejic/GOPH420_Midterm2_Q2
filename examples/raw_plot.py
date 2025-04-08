import numpy as np
import matplotlib.pyplot as plt

def main():
    data_raw = np.loadtxt("../data/rho_vp.txt")

    p = data_raw[:,0]
    v_0 = data_raw[:,1]

    plt.scatter(p,v_0, color='red', s=20)
    plt.xlabel("Rho [g/cm^3]")
    plt.ylabel("V_0 [m/s]")
    plt.title("Raw Plot of Data", fontweight="bold")
    plt.savefig('../figures/Raw_Data.png')

if __name__ == '__main__':
    main()
