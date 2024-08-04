import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_host = os.getenv('API_HOST')
api_key = os.getenv("API_KEY")


def chat(prompt):
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }

    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800
    }

    try:
        response = requests.post(api_host, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()

        if 'choices' in result and result['choices']:
            return result['choices'][0].get('message', {}).get('content', 'No content available.')
        else:
            return "Unexpected response format."
    except requests.RequestException as e:
        return f"Request failed with error: {str(e)}"


if __name__ == '__main__':
    print("Enter 'exit' or 'quit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting chat.")
            break
        response = chat(user_input)
        print(f"GPT: {response}")
