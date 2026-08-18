"""
Simple Python script to interact with OpenAI LLM (ChatGPT).
Requires: openai library and python-dotenv
Install: pip install openai python-dotenv
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

def initialize_client():
    """Initialize OpenAI client with API key from .env file."""
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file. Please add your API key.")
    
    return OpenAI(api_key=api_key)


def chat_with_openai(client, user_message, model="gpt-3.5-turbo"):
    """
    Send a message to OpenAI and get a response.
    
    Args:
        client: OpenAI client instance
        user_message (str): The message to send to the LLM
        model (str): The model to use (default: gpt-3.5-turbo)
        
    Returns:
        str: The response from OpenAI
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    """Main function to interact with OpenAI chatbot."""
    print("=" * 60)
    print("OpenAI Chatbot")
    print("=" * 60)
    
    try:
        # Initialize OpenAI client
        client = initialize_client()
        print("✓ Connected to OpenAI successfully!\n")
        
        while True:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check if user wants to exit
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Assistant: Goodbye! Thanks for chatting with me.")
                break
            
            if not user_input:
                print("Assistant: Please enter a message.\n")
                continue
            
            # Get response from OpenAI
            print("Assistant: ", end="", flush=True)
            response = chat_with_openai(client, user_input)
            print(response)
            print()
            
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print("Please set up your .env file with OPENAI_API_KEY")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
