
import folium

def create_map(center, zoom_start=5):
    return folium.Map(location=center, zoom_start=zoom_start)
