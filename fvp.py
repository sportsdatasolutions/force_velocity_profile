import helpers
import numpy
import pandas as pd

# Read Local Data File #
df = pd.read_csv('./boltfvp.csv', index_col='Athlete', encoding='latin1')

# Deepnote Amazon S3 Connection (SDS Academy S3) #
# !ls /datasets/sdsacademys3/data
# df = pd.read_csv('/datasets/sdsacademys3/data/boltfvp.csv', index_col='Athlete', encoding='latin1')
# df

print('FVP Start')

# Global Variables #
height = 1.95
bodyweight = 94
max_velocity = df["Velocity (m/s)"].max()
tau = 1.3

df["Model Speed (m/s)"] = helpers.model_speed(
    df["Time (s)"], 
    df["Velocity (m/s)"], 
    max_velocity, 
    tau
)

df["Acceleration (m/s2)"] = helpers.model_acceleration(
    df["Time (s)"], 
    df["Velocity (m/s)"], 
    max_velocity, 
    tau
)

df["Force (N)"] = helpers.model_force(
    bodyweight, 
    height, 
    df["Acceleration (m/s2)"], 
    df["Model Speed (m/s)"]
)

df["Force (N/kg)"] = df["Force (N)"] / bodyweight

df["Power (W/kg)"] = df["Force (N/kg)"] * df["Model Speed (m/s)"]

df["Ratio Force (%)"] = helpers.model_ratio_force(
    df["Force (N)"],
    max_velocity,
    bodyweight
)

ratio_of_force_df = df[df["Ratio Force (%)"] < 0.5]

f0_n = helpers.calc_f0_n(df["Model Speed (m/s)"], df["Force (N)"])
fv_profile_slope = helpers.calc_fv_profile_slope(df["Model Speed (m/s)"], df["Force (N/kg)"])
v0_ms = ((f0_n * -1) / bodyweight) / fv_profile_slope
pmax = f0_n * v0_ms / 4
rf_max = ratio_of_force_df["Ratio Force (%)"].iloc[0] * 100
drf = helpers.calc_fv_profile_slope(ratio_of_force_df["Model Speed (m/s)"], ratio_of_force_df["Ratio Force (%)"])

fv_kpi_set = {
    "F0 (N)": f0_n,
    "F0 (N/kg)": f0_n / bodyweight,
    "V0 (m/s)": v0_ms,
    "Pmax (W)": pmax,
    "Pmax (W/kg)": pmax / bodyweight,
    "FV Profile Slope": fv_profile_slope,
    "RFmax": "{}%".format(round(rf_max, 2)),
    "Drf": "{}%".format(round((drf * 100), 2))
}

print('FVP Done')

df.to_csv(r"boltfvp_stats.csv", index=False)

# Deepnote Amazon S3 Connection (SDS Academy S3) #
# df.to_csv(r"/datasets/sdsacademys3/data/boltfvp_stats.csv", index=False)
# !ls /datasets/sdsacademys3/data