# -*- coding: utf-8 -*-
import numpy as np

Temperature_data = [18.5, 19, 20, 25.0, 2, 30, 13.9]
Temperature_array = np.array(Temperature_data)

Avg_Temperature = np.mean(Temperature_array)

Highest_Temperature = np.max(Temperature_array)
Lowest_Temperature = np.min(Temperature_array)

print("Average Temperature:", round(Avg_Temperature, 2), "°C")
print("Highest Temperature:", Highest_Temperature, "°C")
print("Lowest Temperature:", Lowest_Temperature, "°C")

temps_fahrenheit = Temperature_array * 9 / 5 + 32
print("Temperatures in Fahrenheit:", temps_fahrenheit)

hot_day_indices = np.where(Temperature_array > 20)[0]
print("Days with temperatures above 20°C (indices):", hot_day_indices)

