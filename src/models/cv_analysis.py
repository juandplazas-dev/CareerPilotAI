from dataclasses import dataclass


@dataclass
class CVAnalysis:

    score: int
    summary: str

    strengths: list[str]

    weaknesses: list[str]

    technical_skills: list[str]

    soft_skills: list[str]

    recommendations: list[str]

    next_steps: list[str]