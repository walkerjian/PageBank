# Use Python 3.10 for compatibility
FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip \
    && pip install torch==2.2.2 \
                  sentence-transformers==2.2.2 \
                  transformers==4.35.2 \
                  scikit-learn==1.3.2 \
                  networkx \
                  python-dotenv \
                  openai \
                  beautifulsoup4 \
                  requests \
                  huggingface_hub==0.19.4


CMD ["python", "run_demo.py"]
