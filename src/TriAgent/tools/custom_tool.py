# Tools/capabilities to be defined:
# 1. Data Analysis, visualisation of dataframe of biomarkers, target class etc
# 2. AutoML to find best model and most influential weights
# 3. RAG vector db search across various sources (BioRxiv, MedRxiv, optional extra web search -> Vector DB)
# 4. Custom tool for matrix/tensor generation and multiplication (convert array of JSONs to matrix and find similarities)





from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""

    argument: str = Field(..., description="Description of the argument.")


class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."
