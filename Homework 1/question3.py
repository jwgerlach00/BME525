import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative
 

def phi(x):
    if x <= -1:
        return -1
    elif x >= 1:
        return 1
    else:
        return x**3
    
def binarize(x):
    if x < 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    X = np.linspace(-5, 5, 1000)
    phi_of_x = list(map(phi, X))

    # Calculate derivative of function
    deriv_phi = [derivative(phi, x, dx=0.00001) for x in X]

    # Because E = -del(phi) --> NEGATIVE
    neg_E_x = [x for x, p in zip(X, deriv_phi) if p > 0]
    pos_E_x = [x for x, p in zip(X, deriv_phi) if p < 0]
    neut_E_x = [x for x, p in zip(X, deriv_phi) if p == 0]

    # Plot
    plt.plot(X, phi_of_x)
    plt.xlabel('x')
    plt.ylabel('phi')
    plt.locator_params(axis='x', nbins=20)

    # Shade plots
    plt.fill_between(neg_E_x, len(neg_E_x)*[-1.1], [phi(x) for x in neg_E_x])
    plt.fill_between(neut_E_x, len(neut_E_x)*[-1.1], [phi(x) for x in neut_E_x],
                     where=[binarize(x) for x in neut_E_x], color='orange')
    plt.fill_between(neut_E_x, len(neut_E_x)*[-1.1], [phi(x) for x in neut_E_x], 
                     where=[not binarize(x) for x in neut_E_x], color='orange')
    
    # Include 0 has having 0 slope
    plt.plot(1000*[0], np.linspace(-1.1, 0, 1000), color='orange')

    plt.show()
