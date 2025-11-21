# Introduction to Hugging Face

Welcome to this introductory project on Hugging Face! This repository contains examples and tutorials to help you get started with the Hugging Face ecosystem.

## What is Hugging Face?

Hugging Face is a platform and library that provides state-of-the-art Natural Language Processing (NLP) models and tools. It makes it easy to use pre-trained models for various tasks like text classification, question answering, text generation, and more.

## Table of Contents

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Examples](#examples)
  - [Text Classification](#text-classification)
  - [Sentiment Analysis](#sentiment-analysis)
  - [Question Answering](#question-answering)
  - [Text Generation](#text-generation)
  - [Named Entity Recognition](#named-entity-recognition)
- [Resources](#resources)

## Installation

To run the examples in this repository, you'll need Python 3.7 or higher. Install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Getting Started

The `transformers` library by Hugging Face is the main tool we'll use. It provides thousands of pre-trained models for various tasks.

### Basic Usage

```python
from transformers import pipeline

# Create a sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Analyze text
result = classifier("I love learning about AI!")
print(result)
```

## Examples

This repository includes several examples demonstrating different Hugging Face capabilities:

### Text Classification

Learn how to classify text into predefined categories.

```bash
python examples/text_classification.py
```

### Sentiment Analysis

Analyze the sentiment (positive/negative) of text.

```bash
python examples/sentiment_analysis.py
```

### Question Answering

Extract answers from context using pre-trained models.

```bash
python examples/question_answering.py
```

### Text Generation

Generate text using language models.

```bash
python examples/text_generation.py
```

### Named Entity Recognition

Identify and classify named entities in text.

```bash
python examples/named_entity_recognition.py
```

## Project Structure

```
intro-hugging-face/
├── README.md
├── requirements.txt
├── .gitignore
└── examples/
    ├── text_classification.py
    ├── sentiment_analysis.py
    ├── question_answering.py
    ├── text_generation.py
    └── named_entity_recognition.py
```

## Resources

- [Hugging Face Official Website](https://huggingface.co/)
- [Transformers Documentation](https://huggingface.co/docs/transformers)
- [Model Hub](https://huggingface.co/models)
- [Hugging Face Course](https://huggingface.co/course)

## Contributing

Feel free to add more examples or improve existing ones!

## License

This project is for educational purposes.
