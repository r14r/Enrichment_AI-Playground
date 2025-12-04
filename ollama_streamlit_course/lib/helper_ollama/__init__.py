import ollama

def generate(prompt, model="llama3.2", options=None):
    try:
        response = ollama.generate(model=model,prompt=prompt)
        response = response.response
    except Exception as e:
        response = f"Error: {str(e)}"
    
    return response