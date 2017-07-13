"""
Example of how to make a silver sphere  and plot material data,
scattering, absorption, and scattering per multipole
"""

import numpy as np
import matplotlib.pyplot as plt
from miepy.materials import Ag, plot_material
from miepy import sphere

#create a silver material (wavelengths 300-1100nm)
silver = Ag()     #material object

#calculate scattering coefficients
rad = 200       # 200 nm radius
Nmax = 10       # Use up to 10 multipoles
m = sphere(Nmax, silver, rad) #scattering object

# Figure 1: Ag eps & mu data
plt.figure(1)
plot_material(silver)


# Figure 2: Scattering and Absorption
plt.figure(2)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
C,A = m.scattering()     # Returns scat,absorp arrays
plt.plot(m.wav,C,label="Scattering", linewidth=2)
plt.plot(m.wav,A,label="Absorption", linewidth=2)
plt.legend()
plt.xlabel("Wavelength (nm)")
plt.ylabel("Scattering Intensity")

# Figure 3: Scattering per multipole
plt.figure(3)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.plot(m.wav,C,label="Total", linewidth=2)  #plot total scattering
m.plot_scattering_modes(4)    #plots all modes up n=4
plt.legend()
plt.xlabel("Wavelength (nm)")
plt.ylabel("Scattering Intensity")
plt.show()

# Figure 4: Absorption per multipole
plt.figure(4)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.plot(m.wav,A,label="Total", linewidth=2)  #plot total absorption
m.plot_absorption_modes(4)    #plots all modes up n=4
plt.legend()
plt.xlabel("Wavelength (nm)")
plt.ylabel("Absorption Intensity")
plt.show()

# Figure 5: Extinction per multipole
plt.figure(5)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.plot(m.wav,A+C,label="Total", linewidth=2)  #plot total extinction
m.plot_extinction_modes(4)    #plots all modes up n=4
plt.legend()
plt.xlabel("Wavelength (nm)")
plt.ylabel("Extinction Intensity")
plt.show()