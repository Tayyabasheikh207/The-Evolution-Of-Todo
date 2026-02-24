from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import auth, todos


app = FastAPI(title="Todo Web Application API", version="1.0.0")


# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for local development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # Add these for additional flexibility during development
    allow_origin_regex=".*",
    expose_headers=["Access-Control-Allow-Origin"]
)


# Include routers
app.include_router(auth.router, prefix="/auth", tags=["authentication"])
app.include_router(todos.router, prefix="/todos", tags=["todos"])


@app.get("/")
def read_root():
    return {"message": "Todo Web Application API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}