# PageBank: Live Docker Demo

This is a working demonstration of the PageBank project running inside Docker, using GPT-4o via the OpenAI API.

## ✅ Use Case

PageBank scrapes and analyzes webpages, computes PageRank over the discovered link graph, performs semantic search using sentence embeddings, and summarizes the content using GPT-4o. It is containerized with Docker for reproducibility and runs directly from your local code without requiring image rebuilds.

## 🧪 How to Run

From the root of the PageBank repository:

```bash
docker run --rm -it \
  --env-file .env \
  -v "$(pwd)":/app \
  pagebank
```

- `.env` must contain a valid `OPENAI_API_KEY`
- This mounts your current folder to `/app` inside the container
- The code runs live from your latest local version
