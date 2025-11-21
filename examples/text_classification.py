"""
Text Classification Example

This script demonstrates how to use Hugging Face transformers
for text classification tasks.
"""

from transformers import pipeline

def main():
    print("=" * 60)
    print("Text Classification with Hugging Face")
    print("=" * 60)
    print()
    
    # Initialize the text classification pipeline
    # This uses a pre-trained model for zero-shot classification
    print("Loading model...")
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    print("Model loaded successfully!")
    print()
    
    # Example text to classify
    text = "The new smartphone has an amazing camera and long battery life."
    
    # Candidate labels
    candidate_labels = ["technology", "sports", "politics", "entertainment", "business"]
    
    print(f"Text to classify: '{text}'")
    print(f"Candidate labels: {candidate_labels}")
    print()
    
    # Perform classification
    print("Classifying...")
    result = classifier(text, candidate_labels)
    
    # Display results
    print("\nResults:")
    print("-" * 60)
    for label, score in zip(result['labels'], result['scores']):
        print(f"{label:15s}: {score:.4f} ({score*100:.2f}%)")
    print("-" * 60)
    print()
    
    # Another example
    text2 = "The team won the championship after an incredible final match."
    print(f"\nText to classify: '{text2}'")
    print(f"Candidate labels: {candidate_labels}")
    print()
    
    result2 = classifier(text2, candidate_labels)
    
    print("\nResults:")
    print("-" * 60)
    for label, score in zip(result2['labels'], result2['scores']):
        print(f"{label:15s}: {score:.4f} ({score*100:.2f}%)")
    print("-" * 60)

if __name__ == "__main__":
    main()
