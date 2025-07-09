# 🏢 Nearby Business Finder – OpenStreetMap + Google Places

A Python script to **identify and enrich information about nearby businesses** using OpenStreetMap (Overpass API) and Google Places. Useful for market research, site analysis, or enhancing geospatial datasets.

---

## ✅ Features

- Accepts coordinates in both Decimal and DMS formats.
- Queries OpenStreetMap via Overpass API for:
  - Shops, Offices, Industrial, Craft, and Amenities
- Enriches results using Google Places:
  - Address, phone number, and website
- Exports all data to Excel
- Radius-based search (in meters)

---

## 📥 Inputs Required (via terminal)

- `Latitude` – e.g., `41.240019` or `41°14'24.07"N`
- `Longitude` – e.g., `-8.615631` or `8°36'56.27"W`
- `Radius` – e.g., `2000` (in meters)

---

## ⚙️ How It Works

1. Parses user input coordinates.
2. Builds and sends Overpass QL query.
3. Extracts business data from OpenStreetMap.
4. Uses Google Places API to get:
   - Name, Address, Phone, Website
5. Exports combined data to an Excel file with filename based on location.

---

## 🧪 Example Output

If you input:
- Latitude: `41.240019`
- Longitude: `-8.615631`
- Radius: `2000`

Output file example:

businesses_41.24_-8.61563_2000m.xlsx


Columns:
| Name | Category | Latitude | Longitude | Google Name | Address | Phone | Website |

---

## 🔐 Requirements

- Python 3.x
- Packages:
```bash
pip install pandas googlemaps requests openpyxl


🚀 Use Cases
Site suitability and commercial opportunity scouting

Competitor mapping and market profiling

Adding context to GIS-based infrastructure planning



📍 Fast Location-Aware Business Intelligence!