import service

from fastapi import APIRouter
from schemas import CalculateRequest, CalculateResponse

router = APIRouter()

@router.post("/calculate/")
async def calculate(request: CalculateRequest) -> CalculateResponse:
    return await service.calculate(request)
