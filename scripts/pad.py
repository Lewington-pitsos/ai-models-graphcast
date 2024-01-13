center_latitude = -37.75
center_longitude = 145.0

# Set the range
range_degrees = 1.0

# Set the increment
increment = 0.25

# Generating the list of latitudes and longitudes within 2 degrees of the center point
latitudes = [center_latitude + i * increment for i in range(int(-range_degrees / increment), int(range_degrees / increment) + 1)]
longitudes = [center_longitude + i * increment for i in range(int(-range_degrees / increment), int(range_degrees / increment) + 1)]

# Formatting as JSON
result = {
    "latitude": latitudes,
    "longitude": longitudes
}

print(result)
print(len(result['latitude']))

import matplotlib.pyplot as plt

plt.scatter(result['longitude'], result['latitude'])