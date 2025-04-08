import numpy as np
import matplotlib.pyplot as plt

# ln(V_p) = ln(V_0) + k * p

def main():
    data_raw = np.loadtxt("../data/rho_vp.txt")

    p = data_raw[:, 0]
    v_0 = data_raw[:, 1]

    lin_v_0 = np.log(v_0)

    plt.plot(p, lin_v_0)
    plt.show()

if __name__ == '__main__':
    main()