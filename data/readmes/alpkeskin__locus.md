<p align="center">
  <img src="frontend/public/locus-logo.png" alt="Locus Logo" height="36" />
</p>

<h1 align="center">Locus</h1>

<p align="center">
  <strong>Turn street-level photos into GPS coordinates. No metadata required.</strong>
</p>

An open-source AI geolocation system inspired by [GeoSpy](https://geospy.ai/). Identifies locations by detecting and matching building features from photographs using SAM3, ResNet50, and FAISS vector search.

---

## Demo

[![Locus Demo Video](https://img.youtube.com/vi/djmkbBOoho0/0.jpg)](https://www.youtube.com/watch?v=djmkbBOoho0)

---

## How it works

Locus uses a two-phase approach: **Train** to build a location database, and **Search** to identify locations from photos.

### Training Phase

![Training Pipeline](docs/train_diagram.png)

1. **GPS Point Sampling** - Define a center location and radius, system samples GPS points in a circular pattern
2. **Street View Collection** - Fetches multi-directional images (0°, 90°, 180°, 270°) from each point via Google Street View API
3. **Building Detection** - SAM3 (Segment Anything Model) identifies and segments individual buildings in each image
4. **Crop & Normalize** - Extracts each building as a separate 224×224px image
5. **Feature Extraction** - ResNet50 CNN generates 2048-dimensional feature vectors for each building
6. **Vector Indexing** - Stores vectors in FAISS database with GPS metadata for ultra-fast similarity search

**Result**: A searchable database of building features tied to precise GPS coordinates.

### Search Phase

1. **Upload Image** - User provides a street-level photograph
2. **Building Detection** - SAM3 detects buildings in the query image
3. **Feature Extraction** - ResNet50 extracts features from each detected building
4. **Vector Search** - FAISS finds top-5 most similar buildings for each query building
5. **Confidence Filtering** - Filters matches below 0.3 similarity threshold
6. **Location Aggregation** - Groups matches by source image, selects best-matching location
7. **Return Coordinates** - Outputs GPS coordinates with confidence score

**Key Insight**: Instead of matching entire scenes, Locus matches individual buildings. This makes it robust against different angles, times, and weather conditions.

---

## Quick Start

```bash
# Clone and setup
git clone https://github.com/alpkeskin/locus.git
cd locus
cp .env.example .env

# Add your API keys to .env
# - GOOGLE_MAPS_API_KEY (get from console.cloud.google.com)
# - HF_TOKEN (get from huggingface.co/settings/tokens)

# Start with Docker
docker compose up -d

# Access
# Frontend: http://localhost:3000
# API: http://localhost:8000/api/v1/docs
```

---

## API Usage

### Train a location
```bash
curl -X POST http://localhost:8000/api/v1/train \
  -H "Content-Type: application/json" \
  -d '{
    "center_lat": 40.7128,
    "center_lon": -74.0060,
    "radius_meters": 100,
    "num_points": 5
  }'
```

### Find location from image
```bash
curl -X POST http://localhost:8000/api/v1/search \
  -F "file=@/path/to/photo.jpg"
```

Response:
```json
{
  "lat": 40.7128,
  "lon": -74.0060,
  "confidence": 0.87,
  "google_maps_url": "https://www.google.com/maps?q=40.7128,-74.0060"
}
```

---

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.