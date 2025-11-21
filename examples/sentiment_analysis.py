"""
Sentiment Analysis Example

This script demonstrates how to perform sentiment analysis
using Hugging Face transformers.
"""

from transformers import pipeline

def main():
    print("=" * 60)
    print("Sentiment Analysis with Hugging Face")
    print("=" * 60)
    print()
    
    # Initialize the sentiment analysis pipeline
    print("Loading sentiment analysis model...")
    sentiment_analyzer = pipeline("sentiment-analysis")
    print("Model loaded successfully!")
    print()
    
    # Example texts to analyze
    texts = [
        "I absolutely love this product! It's amazing and works perfectly.",
        "This is the worst experience I've ever had. Very disappointed.",
        "The weather is okay today, nothing special.",
        "I'm so excited about the new features! Can't wait to try them all.",
        "This is terrible quality. I want my money back."
    ]
    
    print("Analyzing sentiments...")
    print("-" * 60)
    
    for text in texts:
        # Perform sentiment analysis
        results = sentiment_analyzer(text)
        
        if not results:
            print(f"\nText: '{text}'")
            print("Error: No results returned")
            print("-" * 60)
            continue
        
        result = results[0]
        
        # Display results
        label = result['label']
        score = result['score']
        
        # Format output with emoji
        emoji = "😊" if label == "POSITIVE" else "😞"
        
        print(f"\nText: '{text}'")
        print(f"Sentiment: {label} {emoji}")
        print(f"Confidence: {score:.4f} ({score*100:.2f}%)")
        print("-" * 60)
    
    # Batch processing example
    print("\n\nBatch Processing Example:")
    print("=" * 60)
    
    batch_texts = [
        "Great service!",
        "Poor quality.",
        "Not bad, could be better."
    ]
    
    # Process multiple texts at once
    results = sentiment_analyzer(batch_texts)
    
    for text, result in zip(batch_texts, results):
        emoji = "😊" if result['label'] == "POSITIVE" else "😞"
        print(f"'{text}' -> {result['label']} {emoji} ({result['score']*100:.2f}%)")

if __name__ == "__main__":
    main()
