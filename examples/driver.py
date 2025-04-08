import numpy as np
import matplotlib.pyplot as plt

from src.goph420_M2.regression import multiregression

def main():
    dataRaw = np.loadtxt('../data/rho_vp.txt')

    p = dataRaw[:,0]
    v_0 = dataRaw[:,1]

    y = np.log(v_0)
    Z = np.vstack((np.ones_like(p), p)).T

    coeff, R2 = multiregression(y, Z)

    y_model = Z @ coeff



    plt.figure()
    plt.plot(p, y_model)
    plt.scatter(p, y, color='red', s=15)
    plt.title('Linearized Data with Regression Line')
    plt.xlabel('Rho [g/cm^3]')
    plt.ylabel('Log V_0 [m/s]')
    plt.savefig('../figures/Linearized_Data_With_Regression.png')

    V_0 = np.exp(coeff[0])
    unlinCoeff = [V_0, coeff[1]]
    y_model_raw = unlinCoeff[0] * np.exp(unlinCoeff[1] * p)
    # Sort p and corresponding model values for a clean line plot
    sorted_indices = np.argsort(p)
    p_sorted = p[sorted_indices]
    y_model_raw_sorted= y_model_raw[sorted_indices]

    plt.figure()
    plt.plot(p_sorted, y_model_raw_sorted)
    plt.scatter(p, v_0, color='red', s=15)
    plt.title('Raw Data with Regression Line')
    plt.xlabel('Rho [g/cm^3]')
    plt.ylabel('V_0 [m/s]')
    plt.savefig('../figures/RawData_With_Regression.png')

    print(f'R^2 value: {R2:.4f}')
    print(f'a0 coefficient: {coeff[0]:.4f}')
    print(f'a1 coefficient: {coeff[1]:.4f}')
    print(f'V_0 value is: {V_0:.4f}')


if __name__ == '__main__':
    main()
