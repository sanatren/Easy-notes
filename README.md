# Easy Notes

## Overview
Easy Notes is a full-stack web application built with FastAPI and Bootstrap, designed to help users create, manage, and enhance their note-taking experience with AI-powered smart features. The application provides a clean, intuitive interface for managing notes with advanced capabilities like predictive text and language translation.

## Key Features

### Note Management
- **Create, Read, Update, Delete (CRUD)**: Full functionality for managing notes
- **Important Flag**: Option to mark notes as important for prioritization
- **Responsive Design**: Mobile-friendly interface built with Bootstrap

### AI-Powered Smart Composition
- **Next Word Prediction**: AI-powered suggestions for the next 3 words while typing
- **Tab Key Integration**: Quick word completion using the Tab key
- **LSTM-Based Model**: Utilizes a trained LSTM neural network for accurate word prediction

### Translation Capabilities
- **English to Hindi Translation**: Instant translation of note content
- **Transformer-Based Model**: Uses a fine-tuned transformer model for high-quality translations
- **In-Place Translation**: Translate content directly within the note editor or view

## Technical Architecture

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **Supabase**: PostgreSQL database for data storage
- **Pydantic**: Data validation and settings management
- **TensorFlow**: For deep learning models powering AI features
- **Transformers**: For language translation capabilities

### Frontend
- **HTML/CSS**: Core web technologies
- **Bootstrap 5**: For responsive design and UI components
- **JavaScript**: For client-side interactivity and API calls
- **Jinja2 Templates**: Server-side rendering of HTML pages

### Machine Learning Models
1. **Sentence Predictor**:
   - LSTM-based neural network
   - Trained on text corpus for contextual word prediction
   - Provides real-time suggestions during note composition

2. **English-Hindi Translator**:
   - Fine-tuned transformer model
   - Trained for English to Hindi translation
   - Integrated directly into the note interface

## Project Structure
```
easy-notes/
├── config/               # Configuration files
│   └── db.py             # Database configuration
├── english_to_hindi_translator/ # Translation model files
├── models/               # Data models
│   └── note.py           # Note model definition
├── routes/               # API routes
│   └── note.py           # Note-related endpoints
├── schemas/              # Schema definitions
├── templates/            # HTML templates
│   └── index.html        # Main application page
├── main.py               # Application entry point
├── sentence_predictor.py # Next word prediction functionality
├── translator.py         # Translation functionality
└── README.md             # Project documentation
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Retrieve all notes |
| `/` | POST | Create a new note |
| `/update/{note_id}` | PUT | Update an existing note |
| `/delete/{note_id}` | DELETE | Delete a note |
| `/predict` | POST | Get next word predictions |
| `/translate` | POST | Translate text from English to Hindi |

## Setup and Installation

### Prerequisites
- Python 3.8+
- Node.js and npm (for Bootstrap dependencies)
- Git LFS (for handling large model files)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/easy-notes.git
   cd easy-notes
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install fastapi uvicorn jinja2 python-multipart supabase tensorflow transformers
   ```

4. **Install frontend dependencies**
   ```bash
   npm install
   ```

5. **Pull large model files using Git LFS**
   ```bash
   git lfs pull
   ```

6. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

7. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000`

## Usage Guide

### Creating a Note
1. Fill in the Title, Description, and Content fields
2. Optionally check "Mark as Important" to highlight the note
3. Click "Save Note" to create your note

### Using Smart Composition
1. Start typing in the Content field
2. The system will suggest the next 3 words as you type
3. Press Tab to accept the suggestion

### Translating Note Content
1. Type or select the note content you want to translate
2. Click the "Translate" button below the content field
3. The translated text will appear below the original content

### Editing/Deleting Notes
1. Use the "Edit" button to modify an existing note
2. Use the "Delete" button to remove a note (requires confirmation)

## Development Notes

### Model Training
- The sentence prediction model was trained on a text corpus using TensorFlow
- The English to Hindi translation model is a fine-tuned transformer model

### Supabase Integration
The application uses Supabase as its database backend. The database schema includes a "Notes" table with the following fields:
- id: UUID (primary key)
- Title: String
- description: String
- content: String
- important: Boolean

## Future Enhancements
- User authentication and personal note collections
- Additional language support for translation
- Rich text editing for notes
- Tags and categories for better organization
- Export functionality for notes (PDF, etc.)
- Dark mode support

## Contributors
-  (@[sanatren](https://github.com/sanatren/))


