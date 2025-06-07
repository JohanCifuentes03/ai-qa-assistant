# AI QA Assistant

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Gradio](https://img.shields.io/badge/gradio-3.0+-blueviolet.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Una herramienta de asistencia de IA para la generación de casos de prueba, diseñada para ingenieros de QA. Genera automáticamente casos de prueba funcionales, de rendimiento, seguridad y manuales basados en historias de usuario.

## 🚀 Características

- **Generación de Casos de Prueba**: Crea casos de prueba detallados en múltiples formatos
- **Soporte para Múltiples Tipos de Prueba**:
  - Pruebas Funcionales (Karate DSL)
  - Pruebas de Rendimiento (k6/Karate-Gatling)
  - Pruebas de Seguridad (OWASP API Top 10)
  - Pruebas Manuales (Formato Gherkin)
- **Interfaz Web Interactiva**: Fácil de usar con Gradio
- **Integración con Modelos de IA**: Soporte para OpenAI y Anthropic
- **Personalizable**: Edita y guarda los prompts según tus necesidades

## 🛠️ Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Claves de API para los servicios de IA (OpenAI y/o Anthropic)

## 📦 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/JohanCifuentes03/ai-qa-assistant.git
   cd ai-qa-assistant
   ```

2. Crea y activa un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno:
   - Copia el archivo `.env.example` a `.env`
   - Edita `.env` con tus claves de API

## ⚙️ Configuración

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
# API Keys
OPENAI_API_KEY=tu_api_key_de_openai
ANTHROPIC_API_KEY=tu_api_key_de_anthropic
```

## 🚀 Uso

1. Inicia la aplicación:
   ```bash
   python main.py
   ```

2. Abre tu navegador y ve a `http://localhost:7860`

3. Selecciona el tipo de prueba que deseas generar

4. Ingresa la historia de usuario o requerimientos

5. Haz clic en "Generar Casos de Prueba"

## 📁 Estructura del Proyecto

```
ai-qa-assistant/
├── config/               # Configuración de la aplicación
├── qa-prompts/           # Archivos de prompt para diferentes tipos de pruebas
├── services/             # Lógica de negocio
├── ui/                   # Componentes de la interfaz de usuario
├── utils/                # Utilidades y helpers
├── .env.example          # Ejemplo de archivo de entorno
├── main.py               # Punto de entrada de la aplicación
└── requirements.txt      # Dependencias del proyecto
```

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Por favor, lee nuestras [pautas de contribución](CONTRIBUTING.md) para detalles sobre cómo enviar pull requests.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- [Gradio](https://gradio.app/) - Para la interfaz de usuario
- [OpenAI](https://openai.com/) - Por sus modelos de IA
- [Anthropic](https://www.anthropic.com/) - Por sus modelos Claude
