from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    tags=["root"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"},
        400: {"description": "Bad Request"}
    },
)


@router.get("/")
async def root():
    """Root endpoint.

    Returns:
        dict: A dictionary with a greeting message.
    """
    return {"message": "Hello World"}


@router.get("/health")
async def health():
    """Check the health status of the application.

    Returns:
        dict: A dictionary with a health status message.
    """
    return {"message": "Healthy"}
