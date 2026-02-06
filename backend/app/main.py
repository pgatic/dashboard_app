from fastapi import FastAPI
from app.routes.stats import router as stats_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only; production: allow_origins=["https://tvoj-frontend.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(stats_router, prefix="/api")
