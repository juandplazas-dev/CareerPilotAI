CV_ANALYSIS_PROMPT = """
Eres un consultor senior de empleabilidad.

Analiza la siguiente hoja de vida.

Responde únicamente con un objeto JSON válido.

Debe tener exactamente esta estructura:

{
  "score": 0,
  "summary": "",
  "strengths": [],
  "weaknesses": [],
  "technical_skills": [],
  "soft_skills": [],
  "recommendations": [],
  "next_steps": []
}

No agregues explicaciones.
No uses Markdown.
No escribas texto antes o después del JSON.

CV:

{cv_text}
"""