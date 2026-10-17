# Cloud-Native Microservices Platform for AI Language Models

This repository contains a cloud-native web application built with a microservices architecture. It provides user authentication and a chat interface connected to external language models.

## Overview

The platform includes two backend services and one frontend app:

- Authentication Service: user signup, login, and JWT-protected routes.
- LLM Service: prompt handling and response generation through the Hugging Face inference API (Falcon 7B Instruct).
- Frontend Client: React + Vite interface for authentication and chat.

## Tech Stack

- Node.js + Express
- MongoDB Atlas + Mongoose
- JWT + bcryptjs
- React + TypeScript + Vite
- Axios
- Jest + Supertest (authentication service)
- Docker (authentication service includes a Dockerfile)

## Repository Structure

```text
.
|- client/
|- services/
|  |- authentication-service/
|  |- llm-service/
|- README.md
```

## Services

### 1. Authentication Service

Location: `services/authentication-service`

Features:

- User registration
- User login with JWT issuance
- Protected route with token validation
- MongoDB-backed user storage

Endpoints:

- `POST /api/auth/signup`
- `POST /api/auth/login`
- `GET /api/auth/protected`

Default port:

- `5000` (or `process.env.PORT`)

Environment variables:

- `MONGO_URI`
- `JWT_SECRET`
- `PORT` (optional)

### 2. LLM Service

Location: `services/llm-service`

Features:

- Accepts prompts from the frontend
- Calls Hugging Face Inference API
- Returns generated output to the client

Endpoint:

- `POST /api/llm/generate`

Default port:

- `5001` (or `process.env.PORT`)

Environment variables:

- `HUGGING_FACE_API_KEY`
- `PORT` (optional)

### 3. Frontend Client

Location: `client`

Pages:

- Home (`/`)
- Login (`/login`)
- Signup (`/signup`)
- Chat (`/chat`)

Environment variables:

- `VITE_API_BASE_URL` (used by login/signup API calls)

## Installation and Setup

### Prerequisites

- Node.js 18+ recommended
- npm
- MongoDB Atlas cluster (or compatible MongoDB instance)
- Hugging Face API token

### 1. Clone the Repository

```bash
git clone https://github.com/Codeprojectingfuture/cloud-native-microservices-app.git
cd cloud-native-microservices-app
```

### 2. Configure the Authentication Service

```bash
cd services/authentication-service
npm install
```

Create `.env` in `services/authentication-service`:

```env
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret
PORT=5000
```

Run the service:

```bash
npm run dev
```

Or run in production mode:

```bash
npm start
```

### 3. Configure the LLM Service

```bash
cd ../llm-service
npm install
```

Create `.env` in `services/llm-service`:

```env
HUGGING_FACE_API_KEY=your_hugging_face_api_key
PORT=5001
```

Run the service:

```bash
node server.js
```

### 4. Configure the Frontend Client

```bash
cd ../../client
npm install
```

Create `.env` in `client`:

```env
VITE_API_BASE_URL=http://localhost:5000/api
```

Run the frontend:

```bash
npm run dev
```

## API Reference

### Authentication

`POST /api/auth/signup`

Request body:

```json
{
  "username": "your_name",
  "email": "you@example.com",
  "password": "your_password"
}
```

`POST /api/auth/login`

Request body:

```json
{
  "email": "you@example.com",
  "password": "your_password"
}
```

Response:

```json
{
  "token": "jwt_token"
}
```

`GET /api/auth/protected`

Header:

- `Authorization: Bearer <token>`

### LLM

`POST /api/llm/generate`

Request body:

```json
{
  "prompt": "Explain microservices in simple terms."
}
```

## Testing

Authentication service tests:

```bash
cd services/authentication-service
npm test
```

## Docker

The authentication service includes a Dockerfile.

Build and run locally:

```bash
cd services/authentication-service
docker build -t authentication-service .
docker run -p 5000:5000 --env-file .env authentication-service
```

## Notes and Current Limitations

- The chat page currently posts directly to `http://localhost:5001/api/llm/generate`.
- The login/signup pages use `VITE_API_BASE_URL`.
- There is no root-level Docker Compose file in this repository.
- Multi-model switching (OpenAI/Gemini) is described as future work; Falcon via Hugging Face is currently implemented.

## Future Improvements

- Add request limiting and per-user quotas.
- Add provider abstraction for multiple LLM vendors.
- Add Docker Compose for full local stack.
- Add Kubernetes manifests for deployment orchestration.
