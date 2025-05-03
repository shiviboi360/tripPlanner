# tools/calculator_tools.py

from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool


class TripCalculationInput(BaseModel):
    expression: str = Field(..., description="Mathematical expression to evaluate, e.g., '100 + 250 * 3'")


class TripBudgetCalculatorTool(BaseTool):
    name: str = "Trip Budget Calculator"
    description: str = "Performs mathematical calculations related to trip budgeting."
    args_schema: Type[BaseModel] = TripCalculationInput

    def _run(self, expression: str) -> str:
        try:
            result = eval(expression)
            return f"The result of '{expression}' is {result}."
        except Exception as e:
            return f"❌ Error during calculation: {e}"
