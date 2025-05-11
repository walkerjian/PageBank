#!/bin/bash

# venv_setup.sh — Simple virtual environment setup for PageBank

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$PROJECT_ROOT/.venv"

echo "🔧 Creating virtual environment in $VENV_DIR"
python3 -m venv "$VENV_DIR"

echo "🐍 Activating virtual environment"
source "$VENV_DIR/bin/activate"

echo "📦 Installing requirements"
pip install --upgrade pip
pip install sentence-transformers openai networkx scikit-learn python-dotenv

echo "🧾 Writing requirements.txt"
pip freeze > "$PROJECT_ROOT/requirements.txt"

# .env setup
ENV_FILE="$PROJECT_ROOT/.env"
if [ ! -f "$ENV_FILE" ]; then
    echo "🔐 Creating .env file with placeholder for OpenAI API key"
    echo 'OPENAI_API_KEY="your-api-key-here"' > "$ENV_FILE"
else
    echo "⚠️ .env file already exists, not overwriting"
fi

echo "✅ Setup complete."
echo "👉 To activate: source .venv/bin/activate"
echo "👉 To run:      PYTHONPATH=. python run_demo.py"
