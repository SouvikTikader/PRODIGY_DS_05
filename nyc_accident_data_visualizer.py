import pandas as pd
import folium
from folium.plugins import MarkerCluster, HeatMap
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images directory if it doesn't exist
os.makedirs("images", exist_ok=True)

# Load dataset
df = pd.read_csv("Motor_Vehicle_Collisions_-_Crashes_20250626.csv")

# Combine date and time
df['CRASH DATETIME'] = pd.to_datetime(df['CRASH DATE'] + ' ' + df['CRASH TIME'], errors='coerce')
df['HOUR'] = df['CRASH DATETIME'].dt.hour
df['DAY_OF_WEEK'] = df['CRASH DATETIME'].dt.day_name()

# Clean coordinates
df = df.dropna(subset=['LATITUDE', 'LONGITUDE'])
df = df[(df['LATITUDE'] > 35) & (df['LATITUDE'] < 45) &
        (df['LONGITUDE'] < -70) & (df['LONGITUDE'] > -80)]

# Accident Dot Map (1000 points)
dot_map = folium.Map(location=[40.7128, -74.0060], zoom_start=11, tiles='CartoDB positron')
marker_cluster = MarkerCluster().add_to(dot_map)

for idx, row in df.head(1000).iterrows():
    folium.Marker(
        location=[row['LATITUDE'], row['LONGITUDE']],
        popup=folium.Popup(f"""
            <b>Date:</b> {row['CRASH DATE']}<br>
            <b>Time:</b> {row['CRASH TIME']}<br>
            <b>Injured:</b> {row['NUMBER OF PERSONS INJURED']}<br>
            <b>Killed:</b> {row['NUMBER OF PERSONS KILLED']}<br>
            <b>Factor:</b> {row['CONTRIBUTING FACTOR VEHICLE 1']}
        """, max_width=300),
        icon=folium.Icon(color='red', icon='car', prefix='fa')
    ).add_to(marker_cluster)

map_path = os.path.join("images", "nyc_accident_map.html")
dot_map.save(map_path)
print(f"✅ Accident map saved to '{map_path}'")

# Heatmap
heat_data = df[['LATITUDE', 'LONGITUDE']].head(10000).values.tolist()
heatmap = folium.Map(location=[40.7128, -74.0060], zoom_start=11, tiles='OpenStreetMap')
HeatMap(heat_data, radius=10, blur=15, min_opacity=0.4).add_to(heatmap)
heatmap_path = os.path.join("images", "nyc_accident_heatmap.html")
heatmap.save(heatmap_path)
print(f"✅ Heatmap saved to '{heatmap_path}'")

# Plot 1: Crashes by Hour of Day
plt.figure(figsize=(12, 7))
sns.countplot(x='HOUR', data=df, hue='HOUR', palette='coolwarm', legend=False, zorder=2)
plt.title("Crashes by Hour of Day", fontsize=18)
plt.xlabel("Hour", fontsize=14)
plt.ylabel("Number of Crashes", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, zorder=0)
plt.tight_layout()
plot1_path = os.path.join("images", "crashes_by_hour.png")
plt.savefig(plot1_path, dpi=300)
plt.close()
print(f"✅ Saved: {plot1_path}")

# Plot 2: Crashes by Day of Week 
plt.figure(figsize=(12, 7))
order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sns.countplot(x='DAY_OF_WEEK', data=df, order=order, hue='DAY_OF_WEEK', palette='viridis', legend=False, zorder=2)
plt.title("Crashes by Day of Week", fontsize=18)
plt.xlabel("Day of Week", fontsize=14)
plt.ylabel("Number of Crashes", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, zorder=0)
plt.tight_layout()
plot2_path = os.path.join("images", "crashes_by_day.png")
plt.savefig(plot2_path, dpi=300)
plt.close()
print(f"✅ Saved: {plot2_path}")

# Plot 3: Top Contributing Factors
top_factors = df['CONTRIBUTING FACTOR VEHICLE 1'].value_counts().head(10)
plt.figure(figsize=(12, 8))
sns.barplot(x=top_factors.values, y=top_factors.index,hue=top_factors.index, palette='magma', zorder=2)
plt.title("Top 10 Contributing Factors (Vehicle 1)", fontsize=18)
plt.xlabel("Number of Crashes", fontsize=14)
plt.ylabel("Contributing Factor", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, axis='x', zorder=0)
plt.tight_layout()
plot3_path = os.path.join("images", "top_contributing_factors.png")
plt.savefig(plot3_path, dpi=300)
plt.close()
print(f"✅ Saved: {plot3_path}")
