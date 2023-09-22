import tkinter as tk
import random

# Define some responses for the bot
responses = [
    "Hello!",
    "How are you?",
    "What can I help you with?",
    "Sorry, I don't understand.",
    "Can you please rephrase that?",
    "Goodbye!",
    "That's interesting.",
    "I see.",
    "Tell me more.",
    "I'm not sure, let me think about that.",
    "Let me check on that for you.",
    "Would you like me to do something specific?",
    "I'm here to help.",
    "How can I assist you today?",
    "Is there anything else you would like to discuss?",
    "I'm sorry, I don't have the answer to that right now.",
    "I'm glad we had this conversation."
]

# Define the function that the button will call
def chatbot():
    # Get the user's input
    user_input = input_box.get()

    # Check if the user wants to quit
    if user_input.lower() == "quit":
        output_box.configure(text="Goodbye!")
    else:
        # Generate a random response
        response = random.choice(responses)

        # Update the output box with the response
        output_box.configure(text=response)

    # Clear the input box
    input_box.delete(0, tk.END)

# Create the GUI
root = tk.Tk()
root.title("Chatbot")
root.geometry('400x300')

# Create the input box and label
input_label = tk.Label(root, text="Enter your message:")
input_label.pack()
input_box = tk.Entry(root)
input_box.pack()

# Create the button and attach the chatbot function to it
button = tk.Button(root, text="Send", command=chatbot)
button.pack()

# Create the output box
output_box = tk.Label(root, text="")
output_box.pack()

# Start the main loop
root.mainloop()
