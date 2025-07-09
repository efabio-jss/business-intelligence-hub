import googlemaps
import pandas as pd
import requests
import time
import re

# 🔐 Set your Google Places API Key here
API_KEY = ""
gmaps = googlemaps.Client(key=API_KEY)

# 📌 Converts DMS format to Decimal Degrees
def dms_to_decimal(dms_str):
    dms_str = dms_str.strip().replace("°", " ").replace("'", " ").replace('"', " ")
    parts = re.split(r'\s+', dms_str)
    degrees = float(parts[0])
    minutes = float(parts[1])
    seconds = float(parts[2])
    direction = parts[3].upper()
    decimal = degrees + minutes / 60 + seconds / 3600
    return -decimal if direction in ['S', 'W'] else decimal

# 📥 Input from terminal
lat_input = input("Latitude (e.g., 41.240019 or 41°14'24.07\"N): ").strip()
lon_input = input("Longitude (e.g., -8.615631 or 8°36'56.27\"W): ").strip()
radius = input("Search radius in meters (e.g., 2000): ").strip()

# 📐 Parse coordinate to decimal
def parse_coord(coord):
    return dms_to_decimal(coord) if any(x in coord for x in ['°', "'", '"']) else float(coord)

lat = parse_coord(lat_input)
lon = parse_coord(lon_input)
radius = int(radius)

# 🗺️ Query Overpass API
overpass_url = "http://overpass-api.de/api/interpreter"
query = f"""
[out:json];
(
  node["shop"](around:{radius},{lat},{lon});
  node["office"](around:{radius},{lat},{lon});
  node["craft"](around:{radius},{lat},{lon});
  node["industrial"](around:{radius},{lat},{lon});
  node["amenity"="company"](around:{radius},{lat},{lon});
  way["shop"](around:{radius},{lat},{lon});
  way["office"](around:{radius},{lat},{lon});
  way["craft"](around:{radius},{lat},{lon});
  way["industrial"](around:{radius},{lat},{lon});
);
out center;
"""

print("\n🔎 Searching businesses via OpenStreetMap...")
response = requests.get(overpass_url, params={'data': query})
data = response.json()

# 🧾 Extract businesses
businesses = []
for element in data['elements']:
    tags = element.get('tags', {})
    name = tags.get('name')
    category = tags.get('shop') or tags.get('office') or tags.get('craft') or tags.get('industrial') or tags.get('amenity')
    if name:
        businesses.append({
            'Name': name,
            'Category': category,
            'Latitude': element.get('lat') or element.get('center', {}).get('lat'),
            'Longitude': element.get('lon') or element.get('center', {}).get('lon'),
        })

df = pd.DataFrame(businesses)

if df.empty:
    print("⚠️ No businesses found in this area.")
else:
    print(f"✅ {len(df)} businesses found. Enriching data via Google Places...\n")

    def get_place_details(name, lat, lon):
        try:
            result = gmaps.places(query=name, location=(lat, lon), radius=radius)
            if result['status'] != 'OK' or not result['results']:
                return {}

            place_id = result['results'][0]['place_id']
            details = gmaps.place(place_id=place_id, fields=[
                "name", "formatted_address", "formatted_phone_number", "website"
            ])
            if details['status'] == 'OK':
                info = details['result']
                return {
                    'Google Name': info.get('name'),
                    'Address': info.get('formatted_address'),
                    'Phone': info.get('formatted_phone_number'),
                    'Website': info.get('website')
                }
            return {}
        except Exception as e:
            print(f"Error processing {name}: {e}")
            return {}

    enriched_data = []
    for _, row in df.iterrows():
        info = get_place_details(row['Name'], row['Latitude'], row['Longitude'])
        enriched_data.append(info)
        time.sleep(2)

    df_enriched = pd.DataFrame(enriched_data)
    df_final = pd.concat([df, df_enriched], axis=1)

    output_file = f"businesses_{round(lat, 5)}_{round(lon, 5)}_{radius}m.xlsx"
    df_final.to_excel(output_file, index=False)
    print(f"\n✅ Results saved to: {output_file}")
