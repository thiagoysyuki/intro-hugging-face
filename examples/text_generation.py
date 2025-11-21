"""
Text Generation Example

This script demonstrates how to generate text using
Hugging Face transformers and pre-trained language models.
"""

from transformers import pipeline

def main():
    print("=" * 60)
    print("Text Generation with Hugging Face")
    print("=" * 60)
    print()
    
    # Initialize the text generation pipeline
    print("Loading text generation model...")
    # Using a smaller model for faster inference
    generator = pipeline("text-generation", model="distilgpt2")
    print("Model loaded successfully!")
    print()
    
    # Example prompts for text generation
    prompts = [
        "Artificial intelligence is",
        "The future of technology will",
        "In the world of machine learning,"
    ]
    
    print("Generating text from prompts...")
    print("=" * 60)
    
    for prompt in prompts:
        print(f"\nPrompt: '{prompt}'")
        print("-" * 60)
        
        # Generate text
        results = generator(
            prompt,
            max_length=50,
            num_return_sequences=2,
            temperature=0.7,
            do_sample=True
        )
        
        # Display generated texts
        for i, result in enumerate(results, 1):
            print(f"\nGeneration {i}:")
            print(result['generated_text'])
        
        print("-" * 60)
    
    # Example with different parameters
    print("\n\nCustom Generation Example:")
    print("=" * 60)
    
    custom_prompt = "Once upon a time in a distant land,"
    print(f"\nPrompt: '{custom_prompt}'")
    print("-" * 60)
    
    # Generate with different settings
    custom_results = generator(
        custom_prompt,
        max_length=80,
        num_return_sequences=1,
        temperature=0.9,
        top_p=0.95,
        do_sample=True
    )
    
    print("\nGenerated Story:")
    print(custom_results[0]['generated_text'])
    print("-" * 60)
    
    # Example with more controlled generation
    print("\n\nControlled Generation Example:")
    print("=" * 60)
    
    tech_prompt = "The benefits of open-source software include"
    print(f"\nPrompt: '{tech_prompt}'")
    print("-" * 60)
    
    tech_results = generator(
        tech_prompt,
        max_length=60,
        num_return_sequences=3,
        temperature=0.5,  # Lower temperature for more focused output
        do_sample=True
    )
    
    for i, result in enumerate(tech_results, 1):
        print(f"\nVariation {i}:")
        print(result['generated_text'])
    
    print("-" * 60)

if __name__ == "__main__":
    main()
