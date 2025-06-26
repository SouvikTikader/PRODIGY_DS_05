### 🚗 NYC Traffic Accident Data Visualizer

This project performs **exploratory data analysis and visualization** on NYC motor vehicle collision data. It uses Python to process crash records, visualize patterns by time and contributing factors, and generate interactive maps including **marker clusters** and **heatmaps** of accident locations.

---

### 📁 Dataset

* `Motor_Vehicle_Collisions_-_Crashes_20250626.csv`
  Source: NYC Open Data – [Motor Vehicle Collisions - Crashes](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data)

Each record contains crash details including date, time, location and contributing factors.
This dataset contains records from 26th jan 2025 to 26th june 2025

---

### 📊 Visualizations

All generated charts and maps are saved in the `images/` directory:

| File                           | Description                                     |
| ------------------------------ | ----------------------------------------------- |
| `crashes_by_hour.png`          | Bar chart showing crashes by hour of day        |
| `crashes_by_day.png`           | Bar chart showing crashes by day of the week    |
| `top_contributing_factors.png` | Bar chart of top 10 causes of crashes           |
| `nyc_accident_map.html`        | Interactive folium map with crash location pins |
| `nyc_accident_heatmap.html`    | Interactive heatmap showing accident density    |

---

### ⚙️ Data Processing

After cleaning:

* Removed entries with missing or invalid latitude/longitude
* Filtered to only keep crashes within the NYC bounding box
* Parsed and combined crash date/time into a datetime object
* Extracted hour and day of week for temporal analysis

---

### 🚀 How to Run

#### 1. Clone the Repository

```bash
git clone https://github.com/SouvikTikader/PRODIGY_DS_05.git
cd PRODIGY_DS_05
```

#### 2. Install Required Packages

```bash
pip install pandas folium matplotlib seaborn
```

#### 3. Run the Script

```bash
python nyc_accident_data_visualizer.py
```

The script will:

* Clean and filter the data
* Generate bar charts showing crash trends
* Create a heatmap and marker map for NYC crashes
* Save all outputs to the `images/` directory

---

### 📦 Directory Structure

```
.
├── dataset/
│   └── Motor_Vehicle_Collisions_-_Crashes_20250626.csv
├── images/
│   ├── crashes_by_hour.png
│   ├── crashes_by_day.png
│   ├── top_contributing_factors.png
│   ├── nyc_accident_map.html
│   └── nyc_accident_heatmap.html
├── nyc_accident_data_visualizer.py
└── README.md
```

---

### 📧 Author

**Souvik Tikader**
GitHub: [@SouvikTikader](https://github.com/SouvikTikader)


