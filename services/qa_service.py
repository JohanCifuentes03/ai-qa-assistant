import openai
from anthropic import Anthropic
from config.config import AI_MODELS, OPENAI_API_KEY, ANTHROPIC_API_KEY

class QAService:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
        self.anthropic_client = Anthropic(api_key=ANTHROPIC_API_KEY) if ANTHROPIC_API_KEY else None

    def generate_qa_cases(self, qa_type, user_story, product_context, functional_prompt, 
                        performance_prompt, security_prompt, manual_prompt, ai_model_choice):
        """
        Genera casos de prueba basados en el tipo de QA y el modelo de IA seleccionado
        """
        # Determinar el prompt a usar según el tipo de QA seleccionado
        current_prompt = self._get_current_prompt(qa_type, functional_prompt, 
                                                performance_prompt, security_prompt,
                                                manual_prompt)

        # Combinar contexto y HU con el prompt específico del rol
        full_prompt = f"{product_context}\n\n{current_prompt}\n\nHistoria de Usuario:\n{user_story}"

        try:
            if ai_model_choice == "OpenAI GPT":
                return self._generate_with_openai(full_prompt)
            elif ai_model_choice == "Anthropic Claude":
                return self._generate_with_anthropic(full_prompt)
            else:
                return "Por favor, selecciona un modelo de IA."

        except Exception as e:
            return f"Ocurrió un error al comunicarse con la API de IA: {e}"

    def _get_current_prompt(self, qa_type, functional_prompt, performance_prompt, security_prompt, manual_prompt):
        """Determina el prompt a usar según el tipo de QA"""
        if qa_type == "QA Funcional (Karate DSL)":
            return functional_prompt
        elif qa_type == "QA Performance (k6/Karate-Gatling)":
            return performance_prompt
        elif qa_type == "QA Seguridad (OWASP API Top 10)":
            return security_prompt
        elif qa_type == "QA Funcional Manual":
            return manual_prompt
        else:
            return "Tipo de QA no reconocido."

    def _generate_with_openai(self, prompt):
        """Genera respuesta usando OpenAI"""
        if not self.openai_client:
            return "Error: OpenAI API Key no configurada."
        
        completion = self.openai_client.chat.completions.create(
            model=AI_MODELS["OpenAI GPT"],
            messages=[
                {"role": "system", "content": "Eres un profesional QA AI Engineer experto en calidad e inteligencia artificial."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content

    def _generate_with_anthropic(self, prompt):
        """Genera respuesta usando Anthropic"""
        if not self.anthropic_client:
            return "Error: Anthropic API Key no configurada."
        
        message = self.anthropic_client.messages.create(
            model=AI_MODELS["Anthropic Claude"],
            max_tokens=2000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text
