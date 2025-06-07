def load_prompt_from_file(filepath):
    """Carga el contenido de un archivo de prompt"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Error: Archivo de prompt no encontrado."

def save_prompt_to_file(filepath, content):
    """Guarda el contenido en un archivo de prompt"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def get_default_prompts():
    """Obtiene los prompts por defecto de los archivos"""
    from config.config import DEFAULT_PROMPT_FILES
    
    return {
        "functional": load_prompt_from_file(DEFAULT_PROMPT_FILES["functional"]),
        "performance": load_prompt_from_file(DEFAULT_PROMPT_FILES["performance"]),
        "security": load_prompt_from_file(DEFAULT_PROMPT_FILES["security"]),
        "context": load_prompt_from_file(DEFAULT_PROMPT_FILES["context"])
    }
