"""
Question Answering Example

This script demonstrates how to use Hugging Face transformers
for question answering tasks.
"""

from transformers import pipeline

def main():
    print("=" * 60)
    print("Question Answering with Hugging Face")
    print("=" * 60)
    print()
    
    # Initialize the question answering pipeline
    print("Loading question answering model...")
    qa_pipeline = pipeline("question-answering")
    print("Model loaded successfully!")
    print()
    
    # Context for question answering
    context = """
    Hugging Face is a company that develops tools for building applications using 
    machine learning. It is most notable for its transformers library built for 
    natural language processing applications. The company was founded in 2016 by 
    Clément Delangue, Julien Chaumond, and Thomas Wolf. Hugging Face is headquartered 
    in New York City. The platform allows users to share and collaborate on machine 
    learning models and datasets. As of 2023, Hugging Face has raised over $160 million 
    in funding and is valued at $2 billion.
    """
    
    print("Context:")
    print("-" * 60)
    print(context.strip())
    print("-" * 60)
    print()
    
    # Questions to ask
    questions = [
        "When was Hugging Face founded?",
        "Who founded Hugging Face?",
        "Where is Hugging Face headquartered?",
        "What is Hugging Face most notable for?",
        "What is the valuation of Hugging Face?"
    ]
    
    print("Question Answering Results:")
    print("=" * 60)
    
    for question in questions:
        # Perform question answering
        result = qa_pipeline(question=question, context=context)
        
        # Display results
        print(f"\nQuestion: {question}")
        print(f"Answer: {result['answer']}")
        print(f"Confidence: {result['score']:.4f} ({result['score']*100:.2f}%)")
        print("-" * 60)
    
    # Another example with different context
    print("\n\nAnother Example:")
    print("=" * 60)
    
    context2 = """
    Python is a high-level, interpreted programming language. It was created by 
    Guido van Rossum and first released in 1991. Python emphasizes code readability 
    with its notable use of significant whitespace. Its language constructs and 
    object-oriented approach aim to help programmers write clear, logical code for 
    small and large-scale projects.
    """
    
    print("\nContext:")
    print("-" * 60)
    print(context2.strip())
    print("-" * 60)
    print()
    
    question2 = "Who created Python?"
    result2 = qa_pipeline(question=question2, context=context2)
    
    print(f"\nQuestion: {question2}")
    print(f"Answer: {result2['answer']}")
    print(f"Confidence: {result2['score']:.4f} ({result2['score']*100:.2f}%)")

if __name__ == "__main__":
    main()
