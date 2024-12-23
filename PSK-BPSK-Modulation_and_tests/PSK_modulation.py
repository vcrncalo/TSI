import matplotlib.pyplot as plt
import numpy as np

class Modem:
    """
    Base class for modems.
    
    Attributes:
        M (int): Number of symbols in the constellation.
        constellation (numpy.ndarray): Complex reference constellation points.
        name (str): Name of the modulation scheme.
    """
    def __init__(self, M, constellation, name):
        self.M = M
        self.constellation = constellation
        self.name = name

class PSKModem(Modem):
    """
    Class for generating a Phase-Shift Keying (PSK) modem.
    
    Attributes:
        M (int): Number of symbols in the PSK constellation.
    """
    def __init__(self, M):
        """
        Initialize a PSK modem with M symbols.
        
        Parameters:
            M (int): Number of symbols in the constellation (e.g., 16 for 16-PSK).
        """        
        m = np.arange(0,M)  # all information symbols m={0,1,...,M-1}
        I = 1/np.sqrt(2) * np.cos(m/M * 2 * np.pi)  # In-phase component
        Q = 1/np.sqrt(2) * np.sin(m/M * 2 * np.pi)  # Quadrature component
        constellation = I + 1j * Q  # reference constellation        
        Modem.__init__(self, M, constellation, name='PSK')  # set the modem attributes

def plot_constellation(modem):
    """
    Plot the reference constellation of a modem.
    
    Parameters:
        modem (Modem): Modem object with a defined constellation.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    
    # Plot the constellation with vectors
    ax1.axhline(0, color='k', linestyle='--')
    ax1.axvline(0, color='k', linestyle='--')
    ax1.set_xlabel('Real')
    ax1.set_ylabel('Imaginary')
    ax1.set_title('16_' + modem.name + '_Phasor_Diagram')

    ax1.grid(True)
    
    for point in modem.constellation:
        ax1.arrow(0, 0, point.real, point.imag, head_width=0.05, head_length=0.1, fc='b', ec='b')
    
    # Plot the constellation with points
    ax2.scatter(modem.constellation.real, modem.constellation.imag, s=100, color='b')
    ax2.axhline(0, color='k', linestyle='--')
    ax2.axvline(0, color='k', linestyle='--')
    ax2.set_xlabel('Real')
    ax2.set_ylabel('Imaginary')
    ax2.set_title('16_' + modem.name + '_Constellation')
    
    ax2.grid(True)
    
    plt.show()

def main():
    """
    Main function to demonstrate the PSK modem and plot its constellation.
    
    """
    M = 16
    psk_modem = PSKModem(M)
    plot_constellation(psk_modem)

if __name__ == '__main__':
    main()

