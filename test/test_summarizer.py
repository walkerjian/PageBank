from models.summarizer import summarize_text

text = '''
The Federal Reserve held interest rates steady on Wednesday but left the door open for a hike in the coming months,
citing persistent inflation and a strong labor market.
'''

summary = summarize_text(text)
print("Summary:", summary)
