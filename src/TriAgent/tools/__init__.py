# src/TriAgent/tools/__init__.py

# Classes (tools) defined in directory
__all__ = []

# Tools/capabilities to be defined:
# 1. Data Analysis, visualisation of dataframe of biomarkers, target class etc
# 2. AutoML to find best model and most influential weights
# 3. RAG vector db search across various sources (BioRxiv, MedRxiv, optional extra web search -> Vector DB)
# 4. Custom tool for matrix/tensor generation and multiplication (convert array of JSONs to matrix and find similarities)


################################ HOW TO DEFINE CUSTOM TOOLS ################################## 
# 1. Define input schema 
#   variable = Field(..., description="...")
# 2. Define custom tool:
#   name
#   description
#   args_schema: Type[BaseModel] = input_schema
#   def _run(self, argument: str) -> str:
#       run code, include logic


