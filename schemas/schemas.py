from pydantic import BaseModel, Field

class AlgorithmAnalysis(BaseModel):
    algorithm_name: str = Field(..., title="Algorithm Name", description="The name of the algorithm being analyzed", max_length=100)
    time_complexity: str = Field(..., title="Time Complexity", description="Big-O notation of the algorithm's time complexity", pattern=r"O\([^\)]+\)")
    space_complexity: str = Field(..., title="Space Complexity", description="Big-O notation of the algorithm's space complexity", pattern=r"O\([^\)]+\)")
    is_deterministic: bool = Field(..., title="Deterministic", description="Whether the algorithm is deterministic (True/False)")
    use_case: str = Field(..., title="Use Case", description="A brief description of the algorithm's primary use case", max_length=255)
    input_size: int = Field(..., title="Input Size", description="The size of the input the algorithm operates on", ge=1)
    runtime_performance: float = Field(..., title="Runtime Performance", description="Average runtime performance in seconds", gt=0)
    stability: bool = Field(..., title="Stability", description="Indicates if the algorithm is stable (True/False)")
    implementation_language: str = Field(..., title="Implementation Language", description="The programming language used for the algorithm's implementation", max_length=50)
    description: str = Field(..., title="Description", description="Detailed description of the algorithm", max_length=1000)