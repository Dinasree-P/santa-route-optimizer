# Santa Route Optimizer

An interactive tool for optimizing delivery routes using the Ruin and Recreate algorithm. Built with Streamlit and Folium, this application helps Santa (or any delivery service) find the most efficient route for delivering gifts to multiple locations.

## Features

- **Interactive Location Input:** Add multiple locations by specifying names, latitudes, and longitudes.
- **Ruin and Recreate Optimization:** This custom algorithm refines routes to minimize travel distance.
- **Visual Route Display:** See the optimized route on a map with markers and arrows for clear navigation.
- **Dynamic Feedback:** View and modify location details instantly, with real-time updates on the map.

## Installation

1. **Clone the repository:**
   
   git clone <repository_url>
   cd santa-route-optimizer
   
2. **Install dependencies:**

  pip install streamlit folium streamlit-folium

3. **Run the application:**

 streamlit run <filename>.py

 ## Usage

- **Add Locations**: Open the app and use the input fields to add locations by name, latitude, and longitude.
- **Optimize Route**: Click on **"Find Optimal Route"** to calculate the most efficient path between locations.
- **View Map**: An interactive map displays the optimized route, with markers and arrows indicating each location.

## Code Overview

### `RuinAndRecreate` Class

- **calculate_distances**: Generates a distance matrix with random distances between locations.
- **calculate_route_distance**: Calculates the total distance of a given route.
- **improve_solution**: Applies the ruin and recreate algorithm to find a more efficient route.

### Map Visualization
- **Mapping**: Utilizes `Folium` to generate the map.
- **add_arrows_on_map**: Adds directional markers on the map to indicate the route flow.

## Dependencies

- **streamlit**: For creating an interactive web app.
- **folium**: For map generation and visualization.
- **streamlit_folium**: To integrate Folium maps within Streamlit.

## License

This project is open-source and available for anyone to use or modify.

## Getting Started

1. Clone the repository:

   ```bash
   git clone <repository_url>
   
