# RAG Voice Assistant

A multimodal AI assistant that combines document-based knowledge (RAG) with voice interaction capabilities. The application provides both text and voice interfaces for interacting with your documents.

## Features

- 💬 **Chat Interface**: Text-based interaction with your documents
- 🎙️ **Voice Interface**: Speech-based interaction using wake word detection
- 📚 **Document Management**: Support for multiple document sources
  - PDF documents
  - YouTube videos (auto-transcription)
  - Web pages
- 🔍 **RAG (Retrieval Augmented Generation)**: Smart document querying
- 🔊 **Text-to-Speech**: Natural voice responses

## Prerequisites

- Python 3.9+
- FFmpeg (for audio processing)
- System audio and microphone support

## Installation

1. Clone the repository


2. Create and activate a virtual environment:

```
bash
python -m venv venv
source venv/bin/activate
```


3. Install dependencies:

```
bash
pip install -r requirements.txt
```


4. Set up environment variables:

```
bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
OPENAI_API_KEY=your-api-key-here



## Usage

1. Start the application:

```
bash
streamlit run streamlit_app.py
```


2. Navigate to the different interfaces:
   - 💬 **Chat**: Text-based interaction
   - 🎙️ **Voice**: Speech-based interaction
   - 📚 **Sources**: Document management

### Adding Documents

1. Go to the Sources page
2. Upload documents through one of the supported methods:
   - Upload PDF files
   - Provide YouTube URLs
   - Enter web page URLs

### Voice Interaction

1. Go to the Voice page
2. Use the wake word "hey oak" (configurable)
3. Speak your query
4. Listen to the assistant's response

### Chat Interaction

1. Go to the Chat page
2. Type your question in the input box
3. View the AI's response based on your documents

## Configuration

Key settings can be configured through environment variables or the settings interface:

- `OPENAI_API_KEY`: Your OpenAI API key
- Wake word (default: "hey oak")
- Voice settings (energy threshold, pause duration, etc.)
- Model settings (Whisper model, TTS voice, etc.)

## Project Structure

```
.
├── libs/
│ ├── rag/ # RAG implementation
│ └── voice/ # Voice processing
├── src/
│ ├── components/ # UI components
│ ├── config/ # Configuration
│ ├── pages/ # Application pages
│ └── ui/ # UI implementation
├── data/
│ ├── sources/ # Document storage
│ ├── temp/ # Temporary files
│ └── chroma/ # Vector store
└── streamlit_app.py # Main application
```


## Dependencies

- LangChain: RAG implementation
- OpenAI: Language models and embeddings
- Whisper: Speech-to-text
- ChromaDB: Vector storage
- Streamlit: Web interface
- PyAudio: Audio processing
- FFmpeg: Media processing


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
