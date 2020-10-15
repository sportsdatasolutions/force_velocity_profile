import numpy
import math

# Clean GPS Files #

def clean_gps_data(df):
    df.columns = df.iloc[7]
    df = df.iloc[8:]
    df = df[['Velocity', 'Seconds']].reset_index(drop=True)
    df['Seconds'] = df['Seconds'].astype(float).apply('{:.1f}'.format).astype(float)
    df['Velocity'] = df['Velocity'].astype(float)
    df.columns = ['Velocity (m/s)', 'Time (s)']
    return df

# Identify FVP Scope (based on 1 max run) #

def indentify_fvp_scope(df):
    ## Peak (Max)
    v_max = df['Velocity (m/s)'].max()
    v_max_index = df.index[df['Velocity (m/s)'] == df['Velocity (m/s)'].max()].tolist()[-1]
    ## Start
    v_max_start_index = df.index[df['Time (s)'] == (df['Time (s)'][v_max_index] - 7.0)].tolist()[-1]
    ## Plateau
    v_plateau_index = df.index[df['Time (s)'] == (df['Time (s)'][v_max_index] + 0.2)].tolist()[-1]
    ## Filter to FVP Range
    df = df.iloc[v_max_start_index:v_plateau_index]
    df = df[df['Velocity (m/s)'] > 0.4]
    df["Time (s)"] = ((numpy.arange(df.shape[0]) + 1) / 10.0).astype(float)
    return df

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
