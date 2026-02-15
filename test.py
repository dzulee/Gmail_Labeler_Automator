import torch
from transformers import pipeline
print(f"Is CUDA (GPU) available? {torch.cuda.is_available()}")
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
print("AI Model loaded successfully!")