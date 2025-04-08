import numpy as np
import matplotlib.pyplot as plt

# ln(V_p) = ln(V_0) + k * p

def main():
    data_raw = np.loadtxt("../data/rho_vp.txt")

    p = data_raw[:, 0]
    v_0 = data_raw[:, 1]

    ln_v_0 = np.log(v_0)

    plt.scatter(p, ln_v_0, color='red', s=20)
    plt.xlabel("Rho [g/cm^3]")
    plt.ylabel("Log(V_0) [m/s]")
    plt.title("Linearized Plot of Data", fontweight="bold")
    plt.savefig('../figures/Linearized_Data.png')

if __name__ == '__main__':
    main()