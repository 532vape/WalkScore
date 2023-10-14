import numpy as np

# arbitrary box around UCSB + surrounding area (decimal degrees)
# i got these values by modifying the boundaries of a polyline square generated
# by a .kml file of Isla Vista
lon_min = -119.889848
lon_max = -119.832095
lat_min = 34.406985
lat_max = 34.429613

# Create a grid of longitude and latitude coordinates
# reduced size to 70x70 grid of points since walkscore api daily limit
# is 5000. Can increase later but just for the sake of getting the heatmap
# out fast
lon = np.linspace(lon_min, lon_max, 70)
lat = np.linspace(lat_min, lat_max, 70)

# Save the grid of coordinates to a file
with open("grid.csv", "w") as f:
    for i in range(len(lon)):
      for j in range(len(lat)):
        f.write(f"{lon[i]},{lat[j]}\n")

