import googlemaps
import pandas as pd
import time
import os

# === Insert your Google API Key here ===
API_KEY = ""  # ⚠️ Replace with your actual Google Places API key
gmaps = googlemaps.Client(key=API_KEY)

# === Output folder (customize if needed) ===
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

# === Regions and anchor cities ===
regions = {
    "Catalonia": [
        {"city": "Barcelona", "lat": 41.3851, "lon": 2.1734},
        {"city": "Lleida", "lat": 41.6176, "lon": 0.6200},
        {"city": "Girona", "lat": 41.9794, "lon": 2.8214},
        {"city": "Tarragona", "lat": 41.1189, "lon": 1.2445},
    ],
    "Castilla-La Mancha": [
        {"city": "Toledo", "lat": 39.8628, "lon": -4.0273},
        {"city": "Albacete", "lat": 38.9942, "lon": -1.8585},
        {"city": "Ciudad Real", "lat": 38.9863, "lon": -3.9274},
        {"city": "Cuenca", "lat": 40.0704, "lon": -2.1374},
    ],
    "Andalusia": [
        {"city": "Seville", "lat": 37.3891, "lon": -5.9845},
        {"city": "Málaga", "lat": 36.7213, "lon": -4.4214},
        {"city": "Granada", "lat": 37.1773, "lon": -3.5986},
        {"city": "Córdoba", "lat": 37.8882, "lon": -4.7794},
    ],
    "Galicia": [
        {"city": "Santiago de Compostela", "lat": 42.8782, "lon": -8.5448},
        {"city": "A Coruña", "lat": 43.3623, "lon": -8.4115},
        {"city": "Vigo", "lat": 42.2406, "lon": -8.7207},
        {"city": "Lugo", "lat": 43.0122, "lon": -7.5550},
    ]
}

# === User selects region and radius ===
print("Available regions:")
for i, reg in enumerate(regions.keys(), 1):
    print(f"{i} - {reg}")

choice = int(input("\nSelect region (number): "))
radius = int(input("Search radius in meters (e.g., 30000): "))

region_name = list(regions.keys())[choice - 1]
cities = regions[region_name]

print(f"\n🔎 Searching real estate agencies in {region_name}...\n")

# === Main search process ===
results = []

for city in cities:
    print(f"📍 {city['city']}")
    try:
        response = gmaps.places_nearby(
            location=(city['lat'], city['lon']),
            radius=radius,
            keyword="real estate agency",
            type="real_estate_agency"
        )

        for place in response.get("results", []):
            place_id = place.get("place_id")
            if not place_id:
                continue

            try:
                details = gmaps.place(place_id=place_id, fields=[
                    "name", "formatted_address", "formatted_phone_number", "website",
                    "geometry", "rating", "user_ratings_total"
                ])
                if details["status"] == "OK":
                    info = details["result"]
                    results.append({
                        "Region": region_name,
                        "Base City": city["city"],
                        "Name": info.get("name"),
                        "Address": info.get("formatted_address"),
                        "Phone": info.get("formatted_phone_number"),
                        "Website": info.get("website"),
                        "Latitude": info.get("geometry", {}).get("location", {}).get("lat"),
                        "Longitude": info.get("geometry", {}).get("location", {}).get("lng"),
                        "Rating": info.get("rating"),
                        "Total Reviews": info.get("user_ratings_total"),
                        "Google Place ID": place_id
                    })
                time.sleep(1)
            except Exception as e:
                print(f"⚠️ Error retrieving details for {place.get('name')}: {e}")
                time.sleep(2)
        time.sleep(2)
    except Exception as e:
        print(f"⚠️ Error querying {city['city']}: {e}")
        time.sleep(5)

# === Export results ===
df = pd.DataFrame(results).drop_duplicates(subset="Google Place ID")

output_file = os.path.join(
    output_folder,
    f"real_estate_agencies_{region_name.replace(' ', '_')}_{radius}m.xlsx"
)
df.to_excel(output_file, index=False)

print(f"\n✅ File saved: {output_file}")
print(f"Total agencies found: {len(df)}")
