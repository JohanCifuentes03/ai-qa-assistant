import gradio as gr
from utils.file_utils import get_default_prompts, save_prompt_to_file
from services.qa_service import QAService
from ui.ui_components import UIComponents

def main():
    # Inicializar componentes
    qa_service = QAService()
    ui_components = UIComponents()
    
    # Crear interfaz
    with gr.Blocks(title="QA AI Assistant") as demo:
        gr.Markdown(
            """
            Selecciona un tipo de QA, introduce la Historia de Usuario y genera casos de prueba especializados.
            Puedes ajustar el contexto general y los prompts de cada agente.
            """
        )
        
        # Crear componentes de UI
        save_context_btn, save_context_output = ui_components.create_context_tab()
        ui_components.create_generation_tab()
        
        # Configurar acciones de guardado
        save_context_btn.click(
            fn=lambda x: (save_prompt_to_file(ui_components.DEFAULT_PROMPT_FILES_ABS["context"], x), "Contexto guardado con éxito!"),
            inputs=[ui_components.general_context_input],
            outputs=[save_context_output]
        )
        
        # Configurar generación de casos de prueba
        ui_components.generate_btn.click(
            fn=qa_service.generate_qa_cases,
            inputs=[
                ui_components.qa_type_radio,
                ui_components.user_story_input,
                ui_components.general_context_input,
                ui_components.functional_prompt_input,
                ui_components.performance_prompt_input,
                ui_components.security_prompt_input,
                ui_components.manual_prompt_input,
                ui_components.ai_model_choice
            ],
            outputs=ui_components.output_text
        )
    
    demo.launch()

if __name__ == "__main__":
    main()
