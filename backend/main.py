from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Omogućava frontend da pristupi backend-u
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # može i localhost specifično
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Fake baza podataka
fake_stats = {
    "users": 124,
    "sales": 5320,
    "orders": 87
}

@app.get("/api/stats")
def get_stats():
    return fake_stats
