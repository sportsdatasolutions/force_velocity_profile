import numpy
import math

# Init #

def hello():
    print('Hey')

# Data Helpers #

def model_speed(time, velocity, max_velocity, tau):
    x = (time * -1)/tau
    return max_velocity * (1 - numpy.exp(x))

def model_acceleration(time, velocity, max_velocity, tau):
    x = (time * -1)/tau
    return (max_velocity/tau) * (numpy.exp(x))

def model_force(mass, height, acceleration, model_speed):
    # see Arsac et al. 2002
    force = mass * acceleration
    af = (0.2025 * (height ** 0.725) * (mass ** 0.425)) * 0.266
    air_friction_coef = (0.5 * 1.20 * af * 0.9)
    air_force = air_friction_coef * model_speed * model_speed
    return force + air_force

def model_ratio_force(force, max_velocity, mass):
    resultant_force = numpy.sqrt(((force ** 2) + ((mass * max_velocity) ** 2)))
    return force/resultant_force

# FVP KPIs #

def calc_f0_n(speed, force):
    return numpy.polyfit(speed, force, 1)[1]

def calc_fv_profile_slope(speed, force_kg):
    return numpy.polyfit(speed, force_kg, 1)[0]
