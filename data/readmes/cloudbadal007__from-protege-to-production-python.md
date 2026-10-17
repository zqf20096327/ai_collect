# From Protégé to Production: DineWise Restaurant Recommendation System

This project demonstrates the complete journey from creating an OWL ontology in Protégé to deploying a production-ready Python REST API. The example domain is **DineWise** - a restaurant recommendation system powered by semantic reasoning using Owlready2 and Flask.

## 🚀 Quick Start

**New to this project?** Start here! 👇

👉 **[📖 See QUICKSTART.md for detailed step-by-step instructions](./QUICKSTART.md)**

### ⚡ Get Running in 5 Minutes

```bash
# 1. Clone the repository
git clone https://github.com/cloudbadal007/from-protege-to-production-python.git
cd from-protege-to-production-python

# 2. Create and activate virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Test it works
python load_ontology.py

# 5. Add sample data
python add_data.py

# 6. Start the API
python api.py
```

Then open http://localhost:5000/api/restaurants in your browser! 🎉

**For detailed instructions, troubleshooting, and next steps, see [QUICKSTART.md](./QUICKSTART.md).**

**Want to contribute?** See [CONTRIBUTING.md](./CONTRIBUTING.md).

---

## 🎯 What is DineWise?

DineWise is a semantic web application that uses OWL ontology reasoning to provide intelligent restaurant recommendations. It demonstrates:

- Loading and working with OWL ontologies in Python using Owlready2
- Programmatically adding data to ontologies
- Automatic classification using OWL reasoners
- Building REST APIs that leverage semantic reasoning
- Real-world integration of knowledge graphs with web services

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.8+** (Python 3.9 or higher recommended)
- **pip** (usually comes with Python)
- **Git** (optional, for cloning repository)

**No prior knowledge required!** This is a learning project.

## 📥 Download & Setup

### Option 1: Using Git (Recommended)

```bash
git clone https://github.com/cloudbadal007/from-protege-to-production-python.git
cd from-protege-to-production-python
```

### Option 2: Download ZIP

1. Click the green "Code" button on GitHub
2. Select "Download ZIP"
3. Extract the ZIP file
4. Open terminal in the extracted folder

### Complete Setup

Follow the detailed guide: **[QUICKSTART.md](./QUICKSTART.md)**

## 📖 Usage Guide

### Script 1: Load and Verify Ontology

```bash
python load_ontology.py
```

**Expected Output:**
- Lists all classes in the ontology
- Counts restaurants and dishes
- Displays details of each restaurant

**Purpose:** Verifies that the base ontology (`restaurant-ontology.owl`) loads correctly.

### Script 2: Add Data Programmatically

```bash
python add_data.py
```

**Expected Output:**
- Creates new restaurants (Spice Palace, Pizza Express)
- Adds chefs and dishes
- Saves to `restaurant-ontology-updated.owl`
- Displays summary statistics

**Purpose:** Demonstrates how to programmatically add individuals to an ontology.

### Script 3: Demonstrate Reasoning

```bash
python reasoning_demo.py
```

**Expected Output:**
- Shows dishes marked as vegetarian before reasoning (0)
- Runs the OWL reasoner
- Shows automatically classified VegetarianDish instances (3)
- Queries restaurants serving vegetarian dishes

**Purpose:** Demonstrates automatic classification using OWL reasoners.

### Script 4: Run the REST API

```bash
python api.py
```

**Expected Output:**
```
🔄 Loading ontology...
🧠 Running reasoner...
✅ API ready!

🚀 Starting DineWise API...
📍 API running at: http://localhost:5000

Available endpoints:
  GET  /api/restaurants
  GET  /api/restaurants/<id>
  GET  /api/recommend?vegetarian=true&maxPrice=15
  GET  /api/dishes/vegetarian
  GET  /api/health

Press Ctrl+C to stop
```

**Purpose:** Starts the Flask REST API server.

## 🔌 API Documentation

The DineWise API provides 5 endpoints for interacting with the restaurant ontology:

### 1. GET /api/restaurants

List all restaurants with basic information.

**Example Request:**
```bash
curl http://localhost:5000/api/restaurants
```

**Example Response:**
```json
{
  "success": true,
  "count": 3,
  "data": [
    {
      "id": "SpicePalace",
      "name": "Spice Palace",
      "rating": 4.8,
      "avgPrice": 18.50,
      "address": "123 Curry Lane, Downtown",
      "cuisine": "IndianCuisine"
    }
  ]
}
```

### 2. GET /api/restaurants/<restaurant_id>

Get detailed information about a specific restaurant, including all dishes.

**Example Request:**
```bash
curl http://localhost:5000/api/restaurants/SpicePalace
```

**Example Response:**
```json
{
  "success": true,
  "data": {
    "id": "SpicePalace",
    "name": "Spice Palace",
    "rating": 4.8,
    "avgPrice": 18.50,
    "address": "123 Curry Lane, Downtown",
    "cuisine": "IndianCuisine",
    "dishes": [
      {
        "id": "ButterChicken",
        "name": "Butter Chicken",
        "price": 16.99,
        "isVegetarian": false,
        "spiciness": 3
      },
      {
        "id": "PalakPaneer",
        "name": "Palak Paneer",
        "price": 14.99,
        "isVegetarian": true,
        "spiciness": 2
      }
    ]
  }
}
```

**Error Response (404):**
```json
{
  "success": false,
  "error": "Restaurant 'InvalidID' not found"
}
```

### 3. GET /api/recommend

Get intelligent restaurant recommendations based on filters using ontology reasoning.

**Query Parameters:**
- `vegetarian` (boolean, default: false) - Filter for vegetarian dishes
- `maxPrice` (number, default: 100) - Maximum dish price
- `minRating` (number, default: 0) - Minimum restaurant rating
- `cuisine` (string, optional) - Filter by cuisine type (e.g., "IndianCuisine", "ItalianCuisine")

**Example Request:**
```bash
curl "http://localhost:5000/api/recommend?vegetarian=true&maxPrice=15&minRating=4.0"
```

**Example Response:**
```json
{
  "success": true,
  "filters": {
    "vegetarian": true,
    "maxPrice": 15,
    "minRating": 4.0,
    "cuisine": "any"
  },
  "count": 2,
  "recommendations": [
    {
      "restaurant": "Spice Palace",
      "rating": 4.8,
      "cuisine": "IndianCuisine",
      "dishes": [
        {
          "name": "Palak Paneer",
          "price": 14.99,
          "isVegetarian": true,
          "spiciness": 2
        }
      ]
    }
  ]
}
```

**Example with Cuisine Filter:**
```bash
curl "http://localhost:5000/api/recommend?cuisine=ItalianCuisine&maxPrice=13"
```

### 4. GET /api/dishes/vegetarian

Get all vegetarian dishes using the reasoner's automatic classification.

**Example Request:**
```bash
curl http://localhost:5000/api/dishes/vegetarian
```

**Example Response:**
```json
{
  "success": true,
  "count": 3,
  "data": [
    {
      "name": "Palak Paneer",
      "price": 14.99,
      "restaurant": "Spice Palace",
      "spiciness": 2
    },
    {
      "name": "Margherita Pizza",
      "price": 11.99,
      "restaurant": "Pizza Express",
      "spiciness": 0
    }
  ]
}
```

**Note:** This endpoint uses the reasoner's inferred `VegetarianDish` classification, not just the `isVegetarian` property.

### 5. GET /api/health

Health check endpoint for monitoring and deployment.

**Example Request:**
```bash
curl http://localhost:5000/api/health
```

**Example Response:**
```json
{
  "status": "healthy",
  "ontology_loaded": true,
  "restaurants_count": 3,
  "dishes_count": 5
}
```

## 📁 Project Structure

```
from-protege-to-production-python/
├── restaurant-ontology.owl          # Base ontology from Protégé
├── restaurant-ontology-updated.owl  # After adding data (generated)
├── load_ontology.py                 # Script 1: Load and verify
├── add_data.py                      # Script 2: Add restaurants/dishes
├── reasoning_demo.py                # Script 3: Demonstrate reasoning
├── api.py                           # Script 4: Flask REST API
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git ignore file
└── README.md                        # This file
```

### File Descriptions

- **restaurant-ontology.owl**: Base OWL ontology file with classes, properties, and one sample restaurant (Mama's Trattoria)
- **restaurant-ontology-updated.owl**: Generated file containing additional restaurants and dishes created by `add_data.py`
- **load_ontology.py**: Demonstrates basic ontology loading and inspection
- **add_data.py**: Shows how to programmatically create individuals and relationships
- **reasoning_demo.py**: Demonstrates OWL reasoner's automatic classification capabilities
- **api.py**: Production-ready Flask REST API that uses ontology reasoning for recommendations
- **requirements.txt**: Python package dependencies with exact versions

## 🔑 Key Concepts Demonstrated

### 1. OWL Ontology Loading
- Loading RDF/XML OWL files using Owlready2
- Navigating classes, properties, and individuals
- Safe property access with error handling

### 2. Programmatic Ontology Modification
- Creating new individuals (restaurants, dishes, chefs)
- Setting data properties (name, price, rating)
- Creating object property relationships (serves, specializesIn, worksAt)

### 3. Automatic Reasoning
- Using OWL reasoners to infer new knowledge
- Defined classes (VegetarianDish) with automatic classification
- Querying inferred classifications

### 4. Python Integration
- Object-oriented ontology manipulation
- Type-safe property access
- Exception handling for robust code

### 5. REST API Design
- RESTful endpoint design
- Query parameter filtering
- JSON response formatting
- CORS support for frontend integration
- Error handling with proper HTTP status codes

## 🧪 Testing the API

### Using curl (Command Line)

```bash
# List all restaurants
curl http://localhost:5000/api/restaurants

# Get specific restaurant
curl http://localhost:5000/api/restaurants/SpicePalace

# Get recommendations (vegetarian, max $15)
curl "http://localhost:5000/api/recommend?vegetarian=true&maxPrice=15"

# Get all vegetarian dishes
curl http://localhost:5000/api/dishes/vegetarian

# Health check
curl http://localhost:5000/api/health
```

### Using Python requests

```python
import requests

# List restaurants
response = requests.get('http://localhost:5000/api/restaurants')
print(response.json())

# Get recommendations
params = {
    'vegetarian': True,
    'maxPrice': 15,
    'minRating': 4.0
}
response = requests.get('http://localhost:5000/api/recommend', params=params)
print(response.json())
```

### Using Browser

Simply navigate to:
- http://localhost:5000/api/restaurants
- http://localhost:5000/api/dishes/vegetarian
- http://localhost:5000/api/health

## 🧪 Testing

The project includes a comprehensive test suite using pytest.

### Running Tests

```bash
# Install test dependencies (included in requirements.txt)
pip install -r requirements.txt

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_api.py

# Run specific test
pytest tests/test_api.py::TestAPIRestaurantsEndpoint::test_get_restaurants_success
```

### Test Structure

- **tests/test_load_ontology.py** - Tests for ontology loading
- **tests/test_add_data.py** - Tests for programmatic data addition
- **tests/test_reasoning_demo.py** - Tests for OWL reasoning
- **tests/test_api.py** - Tests for all Flask API endpoints
- **tests/conftest.py** - Shared pytest fixtures

### Test Coverage

The test suite covers:
- ✅ Ontology loading and verification
- ✅ Creating individuals (restaurants, dishes, chefs)
- ✅ Setting properties and relationships
- ✅ OWL reasoner functionality
- ✅ All 5 REST API endpoints
- ✅ Error handling and edge cases

See `tests/README.md` for detailed testing documentation.

## 🐛 Troubleshooting

### Issue: "Could not find 'restaurant-ontology.owl'"

**Solution:** Make sure you're running scripts from the project root directory where `restaurant-ontology.owl` is located.

### Issue: "Could not find 'restaurant-ontology-updated.owl'"

**Solution:** Run `python add_data.py` first to generate the updated ontology file.

### Issue: ModuleNotFoundError for owlready2 or flask

**Solution:** Install dependencies: `pip install -r requirements.txt`

### Issue: Port 5000 already in use

**Solution:** Either stop the other service using port 5000, or modify `api.py` to use a different port:

```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change port to 5001
```

### Issue: Reasoner takes a long time

**Solution:** For larger ontologies, the reasoner may take several seconds. This is normal. The API runs the reasoner once at startup to cache results.

### Issue: VegetarianDish classification not working

**Solution:** Make sure you've run `add_data.py` to create dishes with `isVegetarian=True`, and that `reasoning_demo.py` or `api.py` runs the reasoner with `sync_reasoner(infer_property_values=True)`.

## 📚 Learning Resources

- [Owlready2 Documentation](https://owlready2.readthedocs.io/)
- [OWL 2 Web Ontology Language Primer](https://www.w3.org/TR/owl2-primer/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Protégé Ontology Editor](https://protege.stanford.edu/)

## 🎓 Tutorial Context

This project is the companion code for the tutorial article **"From Protégé to Production: Integrating Your Ontology with Python"**. The tutorial covers:

1. Creating an OWL ontology in Protégé
2. Exporting to RDF/XML format
3. Loading ontologies in Python with Owlready2
4. Adding data programmatically
5. Using OWL reasoners for automatic classification
6. Building production REST APIs
7. Best practices and real-world considerations

## 📝 License

MIT License - feel free to use this code for learning and building your own projects.

## 📂 Documentation

- **[QUICKSTART.md](./QUICKSTART.md)** - ⚡ Step-by-step quick start guide
- **[SETUP_GITHUB.md](./SETUP_GITHUB.md)** - 📤 Guide to upload project to GitHub
- **[CONTRIBUTING.md](./CONTRIBUTING.md)** - 🤝 Contribution guidelines
- **[TEST_SUMMARY.md](./TEST_SUMMARY.md)** - 🧪 Test suite documentation
- **[tests/README.md](./tests/README.md)** - 📋 Testing guide
- **[CHANGELOG.md](./CHANGELOG.md)** - 📝 Project changelog

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

Ways to contribute:
- 🐛 Report bugs or issues
- 💡 Suggest improvements to the code
- 📝 Add more examples or use cases
- 📚 Improve documentation
- ✅ Add more tests
- 🔧 Fix bugs

## 📧 Support

For questions or issues:
- 📖 Check [QUICKSTART.md](./QUICKSTART.md) for setup help
- 🐛 Open an issue on GitHub
- 📚 Read the documentation files
- 💬 Check existing issues for solutions

## 📤 Setting Up on GitHub

Want to upload this project to GitHub? Follow [SETUP_GITHUB.md](./SETUP_GITHUB.md) for step-by-step instructions.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

**Happy coding with OWL ontologies! 🦉🐍**

If you found this project helpful, please consider giving it a ⭐ on GitHub!
