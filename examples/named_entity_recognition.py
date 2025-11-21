"""
Named Entity Recognition (NER) Example

This script demonstrates how to perform Named Entity Recognition
using Hugging Face transformers to identify entities like persons,
organizations, locations, etc. in text.
"""

from transformers import pipeline

def main():
    print("=" * 60)
    print("Named Entity Recognition with Hugging Face")
    print("=" * 60)
    print()
    
    # Initialize the NER pipeline
    print("Loading NER model...")
    ner_pipeline = pipeline("ner", grouped_entities=True)
    print("Model loaded successfully!")
    print()
    
    # Example texts containing various entities
    texts = [
        "Apple Inc. is headquartered in Cupertino, California, and was founded by Steve Jobs.",
        "The Eiffel Tower in Paris, France, attracts millions of tourists every year.",
        "Microsoft CEO Satya Nadella announced new AI features at the conference in Seattle.",
        "The Amazon rainforest spans across Brazil, Peru, Colombia, and several other South American countries.",
        "OpenAI, based in San Francisco, developed ChatGPT which became popular in 2023."
    ]
    
    print("Identifying Named Entities...")
    print("=" * 60)
    
    for text in texts:
        print(f"\nText: '{text}'")
        print("-" * 60)
        
        # Perform NER
        entities = ner_pipeline(text)
        
        if entities:
            print("\nIdentified Entities:")
            for entity in entities:
                entity_text = entity['word']
                entity_type = entity['entity_group']
                score = entity['score']
                
                print(f"  • {entity_text:25s} -> {entity_type:10s} (confidence: {score:.4f})")
        else:
            print("  No entities found.")
        
        print("-" * 60)
    
    # Example with detailed entity types
    print("\n\nDetailed Analysis Example:")
    print("=" * 60)
    
    detailed_text = """
    Barack Obama was the 44th President of the United States. He was born in 
    Honolulu, Hawaii, and studied at Columbia University and Harvard Law School. 
    His administration lasted from 2009 to 2017.
    """
    
    print(f"\nText: {detailed_text.strip()}")
    print("-" * 60)
    
    detailed_entities = ner_pipeline(detailed_text)
    
    # Group entities by type
    entities_by_type = {}
    for entity in detailed_entities:
        entity_type = entity['entity_group']
        if entity_type not in entities_by_type:
            entities_by_type[entity_type] = []
        entities_by_type[entity_type].append(entity['word'])
    
    print("\nEntities grouped by type:")
    for entity_type, words in entities_by_type.items():
        print(f"\n{entity_type}:")
        for word in words:
            print(f"  • {word}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
