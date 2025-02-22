from fastapi import FastAPI
from database import engine, Base
from routers import events, attendees, auth_routes

# Initialize FastAPI application
app = FastAPI(
    title="Event Management API",
    description="An API for managing events and attendees.",
    version="1.0.0",
    docs_url="/docs",  # Custom Swagger docs URL
    redoc_url="/redoc",  # Enable ReDoc UI
)

# Create database tables (ensure all models are initialized)
Base.metadata.create_all(bind=engine)

# Register API routers
app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(attendees.router, prefix="/attendees", tags=["Attendees"])
app.include_router(auth_routes.router, prefix="/auth_routes", tags=["auth_routes"])

# Root endpoint
@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint for the API.
    """
    return {"message": "Welcome to the Event Management API! 🎉"}

