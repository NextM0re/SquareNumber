import asyncio
import time

from schemas import (CalculateRequest,
                     CalculateResponse,
                     SquareResult)

async def square(number: float, delay: float) -> SquareResult:
    start = time.perf_counter()
    await asyncio.sleep(delay)

    return SquareResult(number, number ** 2, delay, round(time.perf_counter() - start, 2))

async def calculate(request: CalculateRequest) -> CalculateResponse:
    tasks = [square(number, delay) for number, delay in zip(request.numbers, request.delays)]

    start = time.perf_counter()
    results = await asyncio.gather(*tasks)

    total_time = round(time.perf_counter() - start, 2)
    return CalculateResponse(results, total_time, total_time < sum(request.delays))
