
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""

# CatBite Delivery Chatbot
# This chatbot helps customers when their cat-themed food order hasn't arrived.

print("Hello! Welcome to CatBite Delivery Support.")
print("Type 'exit' anytime to end the chat.\n")

while True:
    user_message = input("You: ").lower()  # Convert input to lowercase
    
    if "exit" in user_message or "bye" in user_message:
        print("Bot: Thanks for chatting with CatBite Support. Have a purr-fect day!")
        break
    
    elif "food" in user_message and ("late" in user_message or "not arrived" in user_message):
        print("Bot: Oh no, your CatBite order is running late? I’m really sorry about that.")
        order_number = input("Bot: Could you please give me your order number? ")
        print(f"Bot: Thank you. Checking the status for order #{order_number}...")
        print("Bot: It looks like your delivery driver—Whiskers Express—is almost there.")
        print("Bot: We’ll report this delay to our delivery cats and make sure it doesn’t happen again.")
    
    elif "refund" in user_message:
        print("Bot: If your order never arrives, you can request a refund in the CatBite app.")
        print("Bot: Go to 'Orders' -> Select your order -> Tap 'Request Refund'.")
    
    elif "thank" in user_message:
        print("Bot: You’re welcome! We appreciate your patience.")
    
    else:
        print("Bot: I didn’t quite understand that. Could you please rephrase?")
