from dataclasses import dataclass
from pydantic import (BaseModel,
                      Field,
                      NonNegativeFloat,
                      model_validator)
class CalculateRequest(BaseModel):
    numbers: list[float] = Field(examples=[[5, 3, 10]])
    delays: list[NonNegativeFloat] = Field(examples=[[1, 2, 0.5]])

    @model_validator(mode="after")
    def check_lengths(self):
        if len(self.numbers) != len(self.delays):
            raise ValueError("Массивы numbers и delays должны иметь одинаковое кол-во элементов")
        return self

@dataclass
class SquareResult:
    number: float
    square: float
    delay: float
    time: float

@dataclass
class CalculateResponse:
    results: list[SquareResult]
    total_time: float
    parallel_faster_than_sequential: bool
