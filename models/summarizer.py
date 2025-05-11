import openai

openai.api_key = "sk-..."  # Replace with your actual key or use an environment variable

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful summarizer."},
            {"role": "user", "content": f"Summarize this:
{text}"}
        ]
    )
    return response['choices'][0]['message']['content']
