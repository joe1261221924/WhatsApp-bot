import spacy

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Define a set of abusive words (you can customize this)
abusive_words = {"bad", "rude", "offensive", "inappropriate"}

def process_message(message):
    # Tokenize the message
    doc = nlp(message.lower())

    # Check for abusive language
    for token in doc:
        if token.text in abusive_words:
            return "I apologize, but I cannot engage in offensive conversations."

    # Check for greetings
    if any(token.text.lower() in ["hi", "hello", "hey"] for token in doc):
        return "Hello! How can I assist you today?"

    # Respond to other messages
    return "Thank you for your message!"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        response = process_message(user_input)
        print("Bot:", response)
