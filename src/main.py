"""Application entry point for Blog Api."""

from fastapi import FastAPI

from src.routes.health import router as health_router


app = FastAPI(
    title="Blog Api",
    description="A RESTful API for managing blog content, including posts, users, and comments, built with Python and FastAPI, leveraging PostgreSQL for data storage.",
    version="1.0.0",
)

app.include_router(health_router)


@app.get("/")
def root() -> dict[str, str]:
    """Return basic service information."""

    return {
        "service": "blog-api",
        "version": "1.0.0",
        "status": "running",
        "message": "API is running successfully",
    }
