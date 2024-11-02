import streamlit as st
import folium
from streamlit_folium import folium_static
import random

class RuinAndRecreate:
    def __init__(self, locations):
        self.locations = locations
        self.distances = self.calculate_distances()

    def calculate_distances(self):
        distance_matrix = {}
        for i, loc1 in enumerate(self.locations):
            for j, loc2 in enumerate(self.locations):
                if i != j:
                    distance = random.uniform(5, 100)  # Simulated distances
                    distance_matrix[(i, j)] = distance
        return distance_matrix

    def calculate_route_distance(self, route):
        return sum(self.distances[(route[i], route[i + 1])] for i in range(len(route) - 1))

    def improve_solution(self, solution):
        best_distance = self.calculate_route_distance(solution)
        best_solution = solution.copy()

        for i in range(1, len(solution) - 1):
            ruined = solution[i]
            new_solution = [loc for loc in solution if loc != ruined]
            new_solution.insert(random.randint(1, len(new_solution) - 1), ruined)

            new_distance = self.calculate_route_distance(new_solution)
            if new_distance < best_distance:
                best_distance = new_distance
                best_solution = new_solution

        return best_solution, best_distance

def add_arrows_on_map(folium_map, route_coords):
    for i in range(len(route_coords) - 1):
        start = route_coords[i]
        end = route_coords[i + 1]
        # Calculate the midpoint for the arrow
        mid_point = [(start[0] + end[0]) / 2, (start[1] + end[1]) / 2]
        
        # Add a marker as an arrow at the midpoint
        folium.Marker(
            location=mid_point,
            icon=folium.Icon(icon='arrow-up', color='blue')
        ).add_to(folium_map)

def main():
    st.title("Santa Route Optimization using Ruin and Recreate Algorithm")

    if 'locations' not in st.session_state:
        st.session_state.locations = []

    # Input fields for adding locations
    with st.form("Add Location"):
        location_name = st.text_input("Location Name")
        latitude = st.number_input("Latitude", format="%.6f")
        longitude = st.number_input("Longitude", format="%.6f")
        submitted = st.form_submit_button("Add Location")
        
        if submitted and location_name:
            location = {
                'name': location_name,
                'latitude': latitude,
                'longitude': longitude
            }
            st.session_state.locations.append(location)
            st.success(f"Added {location_name} at ({latitude}, {longitude})")

    if st.session_state.locations:
        st.write("Added Locations:")
        for loc in st.session_state.locations:
            st.write(f"{loc['name']} - Latitude: {loc['latitude']}, Longitude: {loc['longitude']}")

    if st.button("Find Optimal Route"):
        if len(st.session_state.locations) > 1:
            rr = RuinAndRecreate(st.session_state.locations)
            initial_solution = list(range(len(st.session_state.locations)))  # Simple initial solution
            best_route, best_distance = rr.improve_solution(initial_solution)

            st.write("Optimal Route:")
            for index in best_route:
                loc = st.session_state.locations[index]
                st.write(f"{loc['name']} (Index: {index})")

            st.write(f"Distance: {best_distance}")

            # Create map to display the route
            map_display = folium.Map(location=[st.session_state.locations[0]['latitude'], st.session_state.locations[0]['longitude']], zoom_start=4)
            for loc in st.session_state.locations:
                folium.Marker([loc['latitude'], loc['longitude']], popup=loc['name']).add_to(map_display)

            # Draw the route on the map
            route_coords = [(st.session_state.locations[i]['latitude'], st.session_state.locations[i]['longitude']) for i in best_route]
            folium.PolyLine(locations=route_coords, color='blue').add_to(map_display)

            # Add arrows on the map
            add_arrows_on_map(map_display, route_coords)

            folium_static(map_display)
        else:
            st.warning("Please add at least two locations to find the optimal route.")

if __name__ == "__main__":
    main()
