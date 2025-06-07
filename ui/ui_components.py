import gradio as gr
import os
from config.config import DEFAULT_PROMPT_FILES, PROMPT_DIR

# Obtener la ruta absoluta de la carpeta de prompts
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPT_DIR_PATH = os.path.join(BASE_DIR, PROMPT_DIR)

# Crear rutas absolutas para los archivos de prompt
DEFAULT_PROMPT_FILES_ABS = {
    "functional": os.path.join(PROMPT_DIR_PATH, "functional_qa_prompt.txt"),
    "performance": os.path.join(PROMPT_DIR_PATH, "performance_qa_prompt.txt"),
    "security": os.path.join(PROMPT_DIR_PATH, "security_qa_prompt.txt"),
    "context": os.path.join(PROMPT_DIR_PATH, "general_context_prompt.txt"),
    "manual": os.path.join(PROMPT_DIR_PATH, "manual_qa_prompt.txt"),
}

class UIComponents:
    def __init__(self):
        self.general_context_input = None
        self.functional_prompt_input = None
        self.performance_prompt_input = None
        self.security_prompt_input = None
        self.ai_model_choice = None
        self.qa_type_radio = None
        self.user_story_input = None
        self.generate_btn = None
        self.output_text = None

    def create_context_tab(self):
        """Crea la pestaña de configuración de contexto"""
        with gr.Tab("Configuración de Agentes y Contexto"):
            gr.Markdown("### Ajusta el Contexto General del Producto")
            self.general_context_input = gr.TextArea(
                label="Contexto General del Producto (afecta a todos los QAs)",
                value=self._load_prompt(DEFAULT_PROMPT_FILES_ABS["context"]),
                lines=5,
                elem_id="general_context_input"
            )
            save_context_btn = gr.Button("Guardar Contexto")
            save_context_output = gr.Textbox(label="Estado de Guardado", interactive=False)

            gr.Markdown("### Prompts de Agentes QA")
            self._create_prompt_tabs()

            return save_context_btn, save_context_output

    def _create_prompt_tabs(self):
        """Crea las pestañas para los prompts de QA"""
        with gr.Tab("QA Funcional (Karate DSL) Prompt"):
            self.functional_prompt_input = gr.TextArea(
                label="Prompt para QA Funcional",
                value=self._load_prompt(DEFAULT_PROMPT_FILES_ABS["functional"]),
                lines=10,
                elem_id="functional_prompt_input"
            )
            save_functional_btn = gr.Button("Guardar Prompt Funcional")
            save_functional_output = gr.Textbox(label="Estado de Guardado", interactive=False)

        with gr.Tab("QA Performance (k6/Karate-Gatling) Prompt"):
            self.performance_prompt_input = gr.TextArea(
                label="Prompt para QA Performance",
                value=self._load_prompt(DEFAULT_PROMPT_FILES_ABS["performance"]),
                lines=10,
                elem_id="performance_prompt_input"
            )
            save_performance_btn = gr.Button("Guardar Prompt Performance")
            save_performance_output = gr.Textbox(label="Estado de Guardado", interactive=False)

        with gr.Tab("QA Seguridad (OWASP API Top 10) Prompt"):
            self.security_prompt_input = gr.TextArea(
                label="Prompt para QA Seguridad",
                value=self._load_prompt(DEFAULT_PROMPT_FILES_ABS["security"]),
                lines=10,
                elem_id="security_prompt_input"
            )
            save_security_btn = gr.Button("Guardar Prompt Seguridad")
            save_security_output = gr.Textbox(label="Estado de Guardado", interactive=False)

        with gr.Tab("QA Funcional Manual Prompt"):
            self.manual_prompt_input = gr.TextArea(
                label="Prompt para QA Funcional Manual",
                value=self._load_prompt(DEFAULT_PROMPT_FILES_ABS["manual"]),
                lines=10,
                elem_id="manual_prompt_input"
            )
            save_manual_btn = gr.Button("Guardar Prompt Manual")
            save_manual_output = gr.Textbox(label="Estado de Guardado", interactive=False)

    def _load_prompt(self, filepath):
        """Carga el contenido de un archivo de prompt"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return "Error: Archivo de prompt no encontrado."

    def create_generation_tab(self):
        """Crea la pestaña de generación de casos de prueba"""
        with gr.Tab("Generar Casos de Prueba"):
            self.ai_model_choice = gr.Radio(
                ["OpenAI GPT", "Anthropic Claude"],
                label="Selecciona Modelo de IA",
                value="OpenAI GPT"
            )

            self.qa_type_radio = gr.Radio(
                ["QA Funcional (Karate DSL)", "QA Performance (k6/Karate-Gatling)", "QA Seguridad (OWASP API Top 10)"],
                label="Selecciona Tipo de QA Asistente"
            )

            self.user_story_input = gr.Textbox(
                label="Historia de Usuario (HU)",
                placeholder="Escribe la historia de usuario con criterios de aceptación aquí...",
                lines=5
            )

            self.generate_btn = gr.Button("Generar Casos de Prueba")

            self.output_text = gr.Markdown(label="Casos de Prueba Generados")
