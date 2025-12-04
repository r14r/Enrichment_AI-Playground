<<<<<<< HEAD
"""
Helper module for Ollama API interactions.

This module provides wrapper functions around the ollama Python SDK
for common use cases in the Streamlit course.
"""

import ollama
from typing import Generator, Optional


def list_models() -> list:
    """
    List all locally available Ollama models.
    
    Returns:
        list: List of model information dictionaries.
    """
    try:
        response = ollama.list()
        return response.get("models", [])
    except Exception as e:
        raise RuntimeError(f"Failed to list models: {e}")


def pull_model(model: str, stream: bool = True) -> Generator:
    """
    Pull/download a model from the Ollama registry.
    
    Args:
        model: Name of the model to pull.
        stream: Whether to stream progress updates.
    
    Yields:
        Progress updates during download.
    """
    try:
        return ollama.pull(model, stream=stream)
    except Exception as e:
        raise RuntimeError(f"Failed to pull model '{model}': {e}")


def chat(
    model: str,
    messages: list,
    stream: bool = False,
    options: Optional[dict] = None,
) -> dict | Generator:
    """
    Send a chat request to an Ollama model.
    
    Args:
        model: Name of the model to use.
        messages: List of message dictionaries with 'role' and 'content' keys.
        stream: Whether to stream the response.
        options: Optional model parameters (temperature, top_p, etc.).
    
    Returns:
        If stream=False: Response dictionary with 'message' key.
        If stream=True: Generator yielding response chunks.
    """
    try:
        kwargs = {"model": model, "messages": messages, "stream": stream}
        if options:
            kwargs["options"] = options
        return ollama.chat(**kwargs)
    except Exception as e:
        raise RuntimeError(f"Chat request failed: {e}")


def generate(
    model: str,
    prompt: str,
    system: Optional[str] = None,
    stream: bool = False,
    options: Optional[dict] = None,
) -> dict | Generator:
    """
    Generate a completion from an Ollama model.
    
    Args:
        model: Name of the model to use.
        prompt: The prompt to generate from.
        system: Optional system prompt.
        stream: Whether to stream the response.
        options: Optional model parameters (temperature, top_p, etc.).
    
    Returns:
        If stream=False: Response dictionary with 'response' key.
        If stream=True: Generator yielding response chunks.
    """
    try:
        kwargs = {"model": model, "prompt": prompt, "stream": stream}
        if system:
            kwargs["system"] = system
        if options:
            kwargs["options"] = options
        return ollama.generate(**kwargs)
    except Exception as e:
        raise RuntimeError(f"Generate request failed: {e}")


def get_chat_response(
    model: str,
    user_message: str,
    system_prompt: Optional[str] = None,
    history: Optional[list] = None,
    temperature: float = 0.7,
) -> str:
    """
    Convenience function to get a simple chat response.
    
    Args:
        model: Name of the model to use.
        user_message: The user's message.
        system_prompt: Optional system prompt to set context.
        history: Optional list of previous messages.
        temperature: Model temperature (0.0 to 1.0).
    
    Returns:
        The assistant's response content as a string.
    """
    messages = []
    
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    
    if history:
        messages.extend(history)
    
    messages.append({"role": "user", "content": user_message})
    
    options = {"temperature": temperature}
    
    response = chat(model=model, messages=messages, options=options)
    return response["message"]["content"]


def stream_chat_response(
    model: str,
    user_message: str,
    system_prompt: Optional[str] = None,
    history: Optional[list] = None,
    temperature: float = 0.7,
) -> Generator:
    """
    Stream a chat response from an Ollama model.
    
    Args:
        model: Name of the model to use.
        user_message: The user's message.
        system_prompt: Optional system prompt to set context.
        history: Optional list of previous messages.
        temperature: Model temperature (0.0 to 1.0).
    
    Yields:
        Response content chunks as strings.
    """
    messages = []
    
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    
    if history:
        messages.extend(history)
    
    messages.append({"role": "user", "content": user_message})
    
    options = {"temperature": temperature}
    
    for chunk in chat(model=model, messages=messages, stream=True, options=options):
        yield chunk["message"]["content"]


def translate_text(
    model: str,
    text: str,
    source_language: str,
    target_language: str,
    temperature: float = 0.3,
) -> str:
    """
    Translate text from one language to another.
    
    Args:
        model: Name of the model to use.
        text: Text to translate.
        source_language: Source language name.
        target_language: Target language name.
        temperature: Model temperature (lower for more consistent translations).
    
    Returns:
        Translated text.
    """
    system_prompt = f"You are a professional translator. Translate the following text from {source_language} to {target_language}. Only provide the translation, no explanations."
    return get_chat_response(
        model=model,
        user_message=text,
        system_prompt=system_prompt,
        temperature=temperature,
    )


def summarize_text(
    model: str,
    text: str,
    max_sentences: int = 3,
    temperature: float = 0.5,
) -> str:
    """
    Summarize a piece of text.
    
    Args:
        model: Name of the model to use.
        text: Text to summarize.
        max_sentences: Maximum number of sentences in the summary.
        temperature: Model temperature.
    
    Returns:
        Summarized text.
    """
    system_prompt = f"You are a summarization expert. Summarize the following text in {max_sentences} sentences or less. Be concise and capture the main points."
    return get_chat_response(
        model=model,
        user_message=text,
        system_prompt=system_prompt,
        temperature=temperature,
    )


def generate_content(
    model: str,
    prompt: str,
    style: str = "professional",
    length: str = "medium",
    temperature: float = 0.7,
) -> str:
    """
    Generate content based on a prompt with specified style and length.
    
    Args:
        model: Name of the model to use.
        prompt: The content generation prompt.
        style: Writing style (professional, casual, creative, technical).
        length: Desired length (short, medium, long).
        temperature: Model temperature.
    
    Returns:
        Generated content.
    """
    length_guide = {
        "short": "Keep it brief, around 2-3 sentences.",
        "medium": "Provide a moderate response, around 1-2 paragraphs.",
        "long": "Provide a detailed response, around 3-4 paragraphs.",
    }
    
    system_prompt = f"You are a content writer. Write in a {style} style. {length_guide.get(length.lower(), length_guide['medium'])}"
    return get_chat_response(
        model=model,
        user_message=prompt,
        system_prompt=system_prompt,
        temperature=temperature,
    )


def answer_question(
    model: str,
    question: str,
    context: Optional[str] = None,
    temperature: float = 0.5,
) -> str:
    """
    Answer a question, optionally using provided context.
    
    Args:
        model: Name of the model to use.
        question: The question to answer.
        context: Optional context/paragraph to answer from.
        temperature: Model temperature.
    
    Returns:
        Answer to the question.
    """
    if context:
        system_prompt = "You are a helpful assistant. Answer the question based only on the provided context. If the answer cannot be found in the context, say so."
        user_message = f"Context:\n{context}\n\nQuestion: {question}"
    else:
        system_prompt = "You are a helpful assistant. Provide clear and accurate answers."
        user_message = question
    
    return get_chat_response(
        model=model,
        user_message=user_message,
        system_prompt=system_prompt,
        temperature=temperature,
    )
=======
import ollama

def generate(prompt, model="llama3.2", options=None):
    try:
        response = ollama.generate(model=model,prompt=prompt)
        response = response.response
    except Exception as e:
        response = f"Error: {str(e)}"
    
    return response
>>>>>>> main
