import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

def ask_chatgpt(question):
    """Send the question to ChatGPT and return the response."""
    try:
        # Make an API call to OpenAI using the new method (Completion)
        response = openai.Completion.create(
            model="text-davinci-003",  # You can replace with any model like "gpt-4"
            prompt=question,
            max_tokens=150
        )

        # Extract and return the answer from the response
        answer = response['choices'][0]['text'].strip()
        return answer

    except Exception as e:
        return f"An error occurred: {e}"

def main():
    question = input("What question do you have? ")
    response = ask_chatgpt(question)
    print("ChatGPT's Response:", response)

if __name__ == "__main__":
    main()
