"""Health check API routes."""

from fastapi import APIRouter


router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("")
def health_check() -> dict[str, str]:
    """Return service health status."""

    return {
        "status": "healthy",
    }
