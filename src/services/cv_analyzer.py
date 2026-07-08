from src.prompts.cv_analysis_prompt import CV_ANALYSIS_PROMPT
from src.services.ai_service import AIService


class CVAnalyzer:

    @staticmethod
    def analyze(cv_text: str):

        prompt = CV_ANALYSIS_PROMPT.format(
            cv_text=cv_text
        )

        return AIService.generate(prompt)