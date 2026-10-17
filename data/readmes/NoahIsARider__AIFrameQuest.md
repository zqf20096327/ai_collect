# AIFrameQuest Project

AIFrameQuest is a modern community discussion platform built with Flask and Vue, supporting user authentication, content management, image search, and more.

In the digital age, we are surrounded by a flood of simulacra (digital images, virtual presences). Hupu's rating system abstracts society into a pure spectacle, where symbols become the only currency; Douban represents a struggle to reclaim subjectivity, but post-truth is not truth — once subjectivity becomes a cliché, popular opinion turns cheap as well.

This software aims to help users build a healthy relationship with digital simulacra by abstracting them into tradable value cards (much like the SEER trading cards we played with as children) and a carefully designed management system, exploring how to maintain cognitive balance in a world where the virtual and the real are intertwined. Only when you endorse a symbol do you become qualified to understand it — just as only when you fall in love with someone can you truly come to know them.

We name our releases after geological eras, because reconstructing a society of simulacra is a long road that requires us to swim upstream before we can go with the flow. We invite you to join us — to find ourselves in the quest to understand the world, and to reshape the world in the process of becoming ourselves.

![Image 1](https://github.com/user-attachments/assets/5e0a1fcd-eeff-4e08-8438-7e7e75ec141e)

![image](https://github.com/user-attachments/assets/0def83a1-4d93-419a-af91-b88c194304c1)

## 🙌 Design Team

Thanks to the following members for their outstanding contributions (in alphabetical order):

[@Dame](https://github.com/dame-byte)

[@Echo](https://github.com/Echo301)

[@Woodzidream](https://github.com/woodzidream)

[@wwwTwilight](https://github.com/wwwTwilight)

[@yixinD777](https://github.com/yixinD777)

## 🌌 Project Overview

This project is a complete full-stack application consisting of the following components:

| Component | Tech Stack | Description |
|---------|-------|------|
| User Frontend | Vue 3 + Element Plus | Frontend interface for regular users |
| Admin Frontend | Vue 3 + Element Plus | Backend management interface for administrators |
| User Backend | Flask | Backend service handling regular user requests |
| Admin Backend | Flask | Backend service handling administrator requests |

## 🔮 Features

- 🔐 User registration and login authentication
- 📝 Multi-category content management (anime, movies, TV series, games, etc.)
- 💬 Comment and rating system
- 🔍 FAISS-based image similarity search
- 🖼️ Static resource serving (image files)
- 📊 RESTful API design
- 👨‍💼 Full-featured admin console
- 🔢 Post view counting and display
- ⭐ User rating system
- 🖼️ Multi-image carousel display
- 💡 User module: image-based Q&A, text-to-image search (multimodal retrieval), and image upload requests
- 🛡️ Admin module: AI-powered automatic moderation of images and comments

## 🏛️ Project Structure

```
AIFrameQuest/
├── backend/                # Backend code
│   ├── app.py             # User backend entry point
│   ├── app-admin.py       # Admin backend entry point
│   ├── requirements.txt   # Backend dependencies
│   ├── data/              # JSON data files
│   ├── images/            # Image storage directory
│   ├── uploads/           # Temporary directory for uploaded files
│   ├── utils/             # User-side utility functions
│   │   ├── faiss_search.py # Image search functionality
│   │   ├── list.py         # Post management functionality
│   │   ├── login.py        # User authentication functionality
│   │   └── views.py        # View counting functionality
│   ├── utils_admin/       # Admin-side utility functions
│   └── utils_database/    # Database-related utilities
│       ├── config.py       # Database configuration
│       ├── init_db.py      # Database initialization script
│       ├── import_data.py  # Data import script
│       ├── models.py       # Database model definitions
│       └── migrate.py      # Database migration script
├── frontend/              # User frontend code
│   ├── src/               # Source code
│   ├── public/            # Static assets
│   ├── package.json       # Frontend dependencies
│   └── vite.config.js     # Vite configuration
└── frontend-admin/        # Admin frontend code
    ├── src/               # Source code
    ├── public/            # Static assets
    ├── package.json       # Frontend dependencies
    └── vite.config.js     # Vite configuration
```

## ⚗️ Environment Requirements

### Backend

- Python >= 3.8
- MySQL >= 5.7

### Frontend

- Node.js >= 16.0.0
- npm >= 7.0.0

## 🚀 Deployment Steps

### 1. Clone the Project

```bash
git clone [repository URL]
cd AIFrameQuest
```

### 2. Configure the Database

#### 2.1 Create the MySQL Database

```sql
CREATE DATABASE aiframequest CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

#### 2.2 Configure the Database Connection

Edit `backend/utils_database/config.py` and update the database connection settings:

```python
# MySQL configuration
MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',            # Change to your own username
    'password': 'your_password',        # Change to your own password
    'database': 'aiframequest'          # Change to the database name you created
}
```

### 3. Deploy the Backend

#### 3.1 Install Backend Dependencies

```bash
cd backend

# Create a virtual environment (recommended)
python -m venv venv

# Activate the virtual environment on Windows
venv\Scripts\activate

# Activate the virtual environment on Linux/Mac
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3.2 Initialize the Database

```bash
# Create database tables
python -m utils_database.init_db

# Import initial data
python -m utils_database.import_data
```

#### 3.3 Start the Backend Services

```bash
# Start the user backend (port 5000)
python app.py

# Start the admin backend in another terminal (port 5001)
python app-admin.py
```

For production, the following deployment methods are recommended:

```bash
# Windows: use Waitress
pip install waitress
waitress-serve --port=5000 app:app
waitress-serve --port=5001 app-admin:app

# Linux/Mac: use Gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
gunicorn -w 4 -b 0.0.0.0:5001 app-admin:app
```

### 4. Deploy the Frontend

#### 4.1 Install Frontend Dependencies and Start the User Frontend

```bash
cd frontend

# Install dependencies
npm install

# Start in development mode
npm run dev

# Or build the production version
npm run build
```

#### 4.2 Install Frontend Dependencies and Start the Admin Frontend

```bash
cd frontend-admin

# Install dependencies
npm install

# Start in development mode
npm run serve

# Or build the production version
npm run build
```

### 5. Configure Frontend Environment Variables

#### 5.1 User Frontend Environment Variables

Create a `.env.development` or `.env.production` file:

```env
VITE_APP_API_BASE_URL=http://localhost:5000  # Backend API base URL
```

#### 5.2 Admin Frontend Environment Variables

Create a `.env.development` or `.env.production` file:

```env
VUE_APP_API_BASE_URL=http://localhost:5001  # Backend API base URL
```

### 6. Deploy with Nginx (Production)

#### 6.1 Nginx Configuration for the User Frontend

```nginx
server {
    listen 80;
    server_name your-domain.com;

    root /path/to/frontend/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /api/ {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /images/ {
        proxy_pass http://127.0.0.1:5000;
    }
}
```

#### 6.2 Nginx Configuration for the Admin Frontend

```nginx
server {
    listen 80;
    server_name admin.your-domain.com;

    root /path/to/frontend-admin/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /api/admin/ {
        proxy_pass http://127.0.0.1:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /admin/images/ {
        proxy_pass http://127.0.0.1:5001;
    }
}
```

## 🌍 Accessing the Application

- User frontend: http://localhost:5173 (development) or http://your-domain.com (production)
- Admin frontend: http://localhost:8080 (development) or http://admin.your-domain.com (production)
- User backend API: http://localhost:5000
- Admin backend API: http://localhost:5001

## 🗿 Frequently Asked Questions

### 1. Database Connection Issues

- Make sure the MySQL service is running
- Check that the username and password are correct
- Make sure the database name is correct

### 2. Image Similarity Search Issues

- Make sure FAISS and PyTorch are installed
- Check that the image directory permissions are correct
- Make sure the image formats are supported (JPG, PNG)

### 3. Frontend Build Issues

- Make sure the Node.js and npm versions meet the requirements
- Check that the environment variables are configured correctly
- Make sure all dependencies are installed correctly

### 4. View Counting Issues

- Make sure the frontend correctly calls the API that updates view counts
- Check that the `views` field in the database is updated correctly

## 🗺️ Development Roadmap

### Archean: Beta

**Core goal**: Validate the feasibility of the basic interaction model

```plaintext
📌 Technical implementation:
- Build an image upload/retrieval prototype with vanilla JavaScript
- Validate basic button clicks and data display interactions
- Simulate data storage with local JSON files in the browser

🔍 Naming rationale:
Analogous to the origin of life on Earth — establishing the most primitive foundation of the system architecture
```

### Cambrian: V1

**Core goal**: Build the framework for the basic feature modules

```plaintext
📌 Technical implementation:
- Build the frontend interface with Vue3 + Element Plus
- Implement account registration / image search / five-star rating features
- Develop a simple backend API with Flask

🔍 Naming rationale:
Like the Cambrian explosion of life, achieving rapid iteration of feature modules
```

### Ordovician: V2

**Core goal**: Enhance system stability and extensibility

```plaintext
📌 Technical implementation:
- Replace local JSON storage with MySQL for user data
- Add an entry/term application feature
- Admin console (basic permission control + data dashboard)
- Ingest 1000+ mock image/entry records (Xiaohongshu crawler)
- Deep-learning-based comment sentiment analysis

🔍 Naming rationale:
Corresponding to the ecological complexity of the Ordovician, the system begins to support multi-role collaboration
```

### Holocene: V3

**Core goal**: Improve user experience and data integrity

```plaintext
📌 Technical implementation:
- Visual redesign of the interface
- Optimize component load speed and interaction animations
- Cloud deployment (inspired by the week-3 exploratory task)
- Multimodal search functionality (inspired by the week-3 exploratory task)
- User interactive games (inspired by the week-3 exploratory task)

🔍 Naming rationale:
Symbolizing the maturity of human civilization, the system enters an easy-to-use and stable stage
```

### Anthropocene: V4

**Core goal**: Introduce intelligent management mechanisms

```plaintext
📌 Technical implementation:
- Semi-automated entry moderation workflow powered by large models
- Integration with major websites (tentatively via MCP)

🔍 Naming rationale:
Echoing the age of artificial intelligence, establishing a human-machine collaborative boundary for content governance
```

## ⚖️ License

[MIT License](LICENSE)

## 🪨 Contact

If you have any questions or suggestions, please submit an Issue or contact the project maintainers.
