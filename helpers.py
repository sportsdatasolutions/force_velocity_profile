import numpy
import math

def hello():
    print('Hey')

def model_speed(time, velocity, max_velocity, tau):
    x = (time * -1)/tau
    return max_velocity * (1 - numpy.exp(x))

def model_acceleration(time, velocity, max_velocity, tau):
    x = (time * -1)/tau
    return (max_velocity/tau) * (numpy.exp(x))

def model_force(time, velocity, max_velocity, mass, height, acceleration, model_speed):
    total_force = calculate_force(mass, height, acceleration, model_speed)
    return total_force/mass

def model_ratio_force(max_velocity, mass, height, acceleration, model_speed):
    total_force = calculate_force(mass, height, acceleration, model_speed)
    resultant_force = numpy.sqrt(((total_force ** 2) + ((mass * max_velocity) ** 2)))
    return total_force/resultant_force

def calculate_force(mass, height, acceleration, model_speed):
    # see Arsac et al. 2002
    force = mass * acceleration
    af = (0.2025 * (height ** 0.725) * (mass ** 0.425)) * 0.266
    air_friction_coef = (0.5 * 1.20 * af * 0.9)
    air_force = air_friction_coef * model_speed*model_speed
    return force + air_force