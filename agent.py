import requests
import json

endpoint = "https://YOUR_DEPLOYMENT_NAME.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT_NAME/chat/completions?api-version=2024-02-15-preview"
api_key = "YOUR_API_KEY"

headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}


def chat_with_gpt(prompt):
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
        response = requests.post(endpoint, headers=headers, json=data)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.RequestException as e:
        return f"Failed, Code: {response.status_code}\n{e}"


while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting chat.")
        break
    response = chat_with_gpt(user_input)
    print(f"GPT: {response}")
