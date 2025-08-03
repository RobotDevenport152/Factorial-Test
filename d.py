import numpy as np

rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

rainfall_array = np.array(rainfall)
print("Rainfall array:", rainfall_array)

total_rainfall = np.sum(rainfall_array)
print("Total rainfall:", f"{total_rainfall:.2f} mm")

average_rainfall = np.mean(rainfall_array)
print("Average rainfall:", f"{average_rainfall:.2f} mm")

dry_days = np.sum(rainfall_array == 0)
print("Number of dry days:", dry_days)

heavy_rain_days = np.where(rainfall_array > 5)[0]
print("Days with rainfall > 5 mm:", heavy_rain_days)

percentile_75 = np.percentile(rainfall_array, 75)
above_75th = rainfall_array[rainfall_array > percentile_75]
print("75th percentile:", f"{percentile_75:.2f} mm")
print("Rainfall values above 75th percentile:", [f"{v:.2f} mm" for v in above_75th])
