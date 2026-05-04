# Dashboard App

A local development dashboard with a FastAPI backend and a React/Vite frontend. The backend and frontend live in separate folders inside this project.

## Tech Stack

- Backend: Python, FastAPI, Uvicorn, SQLAlchemy, SQLite
- Frontend: React, Vite, Tailwind CSS, Recharts

## Backend

```bash
cd backend
conda activate dashboard_env
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

The backend runs at `http://127.0.0.1:8000` by default.

## Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend runs on the Vite development server.

## Running the App

Start the backend and frontend in separate terminals so both development servers stay running.

## API

- `GET /api/stats`

## Notes

This project is set up for local development. Configuration, CORS, and the SQLite database are not production-ready.
