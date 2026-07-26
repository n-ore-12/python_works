import numpy as np 
from scipy.constants import speed_of_light

def pendulum_period(length):
    period = 2 * np.pi * np.sqrt(length / 9.81)
    return period

def initial_pressure(initial_volume, final_volume, final_pressure):
    pressure = (final_pressure * final_volume) / initial_volume
    return pressure

def circular_orbit_velocity(radius, period):
    velocity = (2 * np.pi * radius) / period
    return velocity

def galactic_velocity(wavelength_shift, reference_wavelength):
    gal_velocity = (wavelength_shift / reference_wavelength) * speed_of_light
    return gal_velocity

print(pendulum_period(3))
print(initial_pressure(100, 500, 101))
print (circular_orbit_velocity(20, 8000))



