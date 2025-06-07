import os
from dotenv import load_dotenv

load_dotenv()

# Configuración de API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Rutas de archivos
PROMPT_DIR = "qa-prompts"
PROMPT_DIR_PATH = os.path.join(os.getcwd(), PROMPT_DIR)
DEFAULT_PROMPT_FILES = {
    "functional": os.path.join(PROMPT_DIR, "functional_qa_prompt.txt"),
    "performance": os.path.join(PROMPT_DIR, "performance_qa_prompt.txt"),
    "security": os.path.join(PROMPT_DIR, "security_qa_prompt.txt"),
    "manual": os.path.join(PROMPT_DIR, "manual_qa_prompt.txt"),
    "context": os.path.join(PROMPT_DIR, "general_context_prompt.txt")
}
DEFAULT_PROMPT_FILES_ABS = {
    "functional": os.path.join(PROMPT_DIR_PATH, "functional_qa_prompt.txt"),
    "performance": os.path.join(PROMPT_DIR_PATH, "performance_qa_prompt.txt"),
    "security": os.path.join(PROMPT_DIR_PATH, "security_qa_prompt.txt"),
    "manual": os.path.join(PROMPT_DIR_PATH, "manual_qa_prompt.txt"),
    "context": os.path.join(PROMPT_DIR_PATH, "general_context_prompt.txt")
}

# Modelos disponibles
AI_MODELS = {
    "OpenAI GPT": "gpt-4o",
    "Anthropic Claude": "claude-3-opus-20240229"
}

# Tipos de QA
QA_TYPES = {
    "QA Funcional (Karate DSL)": "functional",
    "QA Performance (k6/Karate-Gatling)": "performance",
    "QA Seguridad (OWASP API Top 10)": "security",
    "QA Funcional Manual": "manual"
}
