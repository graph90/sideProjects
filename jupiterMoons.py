import math
from datetime import datetime, timedelta

orbital_periods = {
    "Io": 1.769, 
    "Europa": 3.551, 
    "Ganymede": 7.155, 
    "Callisto": 16.689
}

semi_major_axes = {
    "Io": 421700, 
    "Europa": 671034, 
    "Ganymede": 1070412, 
    "Callisto": 1882709
}

epoch = datetime(2000, 1, 1)

def get_moon_phase(moon, date):
    days_since_epoch = (date - epoch).total_seconds() / (24 * 3600)
    mean_anomaly = 2 * math.pi * (days_since_epoch % orbital_periods[moon]) / orbital_periods[moon]
    x = semi_major_axes[moon] * math.cos(mean_anomaly)
    y = semi_major_axes[moon] * math.sin(mean_anomaly)
    jupiter_shadow_radius = 142984 / 2
    distance_from_jupiter = math.sqrt(x**2 + y**2)
    
    if distance_from_jupiter < jupiter_shadow_radius:
        phase = "Eclipsed (in shadow)"
    else:
        phase = "Illuminated"
    
    return phase

def get_all_moon_phases(date):
    phases = {}
    for moon in orbital_periods:
        phases[moon] = get_moon_phase(moon, date)
    return phases

date = datetime.now()
moon_phases = get_all_moon_phases(date)

print("Phases of Jupiter's moons on", date.strftime("%Y-%m-%d %H:%M:%S"))
for moon, phase in moon_phases.items():
    print(f"{moon}: {phase}")
