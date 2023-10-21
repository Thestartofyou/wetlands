import geopandas as gpd
import matplotlib.pyplot as plt

# Load the wetlands shapefile (replace with your own file)
wetlands_shapefile = "path/to/your/wetlands_shapefile.shp"

# Read the shapefile using geopandas
wetlands = gpd.read_file(wetlands_shapefile)

# Create a plot of the wetlands
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
wetlands.plot(ax=ax, cmap="Blues")  # You can choose a suitable colormap

# Set a title for the map
ax.set_title("Wetlands Tracking")

# Display the map
plt.show()
