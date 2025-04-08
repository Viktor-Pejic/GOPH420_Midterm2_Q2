import numpy as np
import matplotlib.pyplot as plt

def main():
    data_raw = np.loadtxt("../data/rho_vp.txt")

    rho = data_raw[:,0]
    v_p = data_raw[:,1]

    plt.plot(rho,v_p)
    plt.show()

if __name__ == '__main__':
    main()
