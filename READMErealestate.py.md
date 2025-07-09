# 🏠 Real Estate Agencies Extractor (Google Places)

This Python script automates the extraction of **real estate agency data** across several Spanish regions using the **Google Places API**. It performs structured searches by city and region, enriches results with business details, and exports to Excel.

---

## ✅ Features

- Region-based search (Catalonia, Galicia, Andalusia, Castilla-La Mancha)
- Cities pre-defined for each region
- Uses:
  - Google Places Nearby Search (`real estate agency`)
  - Google Place Details API
- Extracted data includes:
  - Name, Address, Phone, Website
  - Location (Lat/Lon), Rating, Reviews
- Duplicate removal by Google Place ID
- Output saved to Excel

---

## 📍 Regions Included

- Catalonia (Barcelona, Girona, Lleida, Tarragona)
- Castilla-La Mancha (Toledo, Albacete, Ciudad Real, Cuenca)
- Andalusia (Seville, Málaga, Granada, Córdoba)
- Galicia (Vigo, A Coruña, Santiago de Compostela, Lugo)

Can be configurated to other regions and countries 
---

## 💾 Output Example
real_estate_agencies_Catalonia_30000m.xlsx


Columns:
| Region | Base City | Name | Address | Phone | Website | Latitude | Longitude | Rating | Total Reviews | Google Place ID |

---

## ⚙️ How It Works

1. User selects region and radius.
2. Script queries each city for real estate agencies.
3. Fetches business details from Google.
4. Stores and de-duplicates the results.
5. Saves to Excel.

---

## 🔐 Requirements

- Python 3.x
- Install dependencies:
```bash
pip install pandas googlemaps openpyxl



