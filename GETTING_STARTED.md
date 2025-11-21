# Getting Started Guide

This guide will help you set up and run the Hugging Face examples in this repository.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/thiagoysyuki/intro-hugging-face.git
cd intro-hugging-face
```

### 2. (Optional) Create a Virtual Environment

It's recommended to use a virtual environment to avoid conflicts with other Python packages.

**On Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** The first time you run the examples, the models will be downloaded automatically. This may take a few minutes depending on your internet connection. The models are cached locally, so subsequent runs will be faster.

## Running the Examples

Once the dependencies are installed, you can run any of the examples:

### Sentiment Analysis
```bash
python examples/sentiment_analysis.py
```

This example analyzes the sentiment (positive/negative) of various texts.

### Text Classification
```bash
python examples/text_classification.py
```

This example demonstrates zero-shot text classification.

### Question Answering
```bash
python examples/question_answering.py
```

This example shows how to extract answers from context.

### Text Generation
```bash
python examples/text_generation.py
```

This example generates text based on prompts using GPT-2.

### Named Entity Recognition
```bash
python examples/named_entity_recognition.py
```

This example identifies named entities (persons, organizations, locations) in text.

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'transformers'"
**Solution:** Make sure you've installed the requirements:
```bash
pip install -r requirements.txt
```

### Issue: Models downloading slowly
**Solution:** The first time you run an example, Hugging Face will download the required models. This is normal and only happens once. The models are cached in `~/.cache/huggingface/`.

### Issue: Out of memory errors
**Solution:** Some models are large and require significant RAM. If you encounter memory issues, try:
- Closing other applications
- Using a smaller model (you can modify the examples to use different models)
- Running examples one at a time

## Next Steps

After running the examples, you can:

1. Modify the example texts to test with your own data
2. Try different models from the [Hugging Face Model Hub](https://huggingface.co/models)
3. Explore the [Hugging Face documentation](https://huggingface.co/docs/transformers) for more advanced features
4. Build your own applications using the transformers library

## Additional Resources

- [Hugging Face Course](https://huggingface.co/course) - Free course on NLP with transformers
- [Transformers Documentation](https://huggingface.co/docs/transformers)
- [Model Hub](https://huggingface.co/models) - Browse thousands of pre-trained models
- [Datasets](https://huggingface.co/datasets) - Access various datasets for training and evaluation

## Support

If you encounter issues or have questions:
- Check the [Hugging Face Forums](https://discuss.huggingface.co/)
- Review the [GitHub Issues](https://github.com/huggingface/transformers/issues) for the transformers library
- Read the official documentation

Happy learning! 🤗
