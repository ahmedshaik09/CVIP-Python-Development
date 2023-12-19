import random
import time

def get_random_text():
    # List of sentences for typing practice
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a powerful programming language.",
        "Practice makes perfect.",
        "Coding is fun and rewarding.",
        "Typing speed matters in today's world."
    ]
    return random.choice(texts)

def calculate_accuracy(original_text, typed_text):
    correct_chars = sum(1 for a, b in zip(original_text, typed_text) if a == b)
    accuracy = (correct_chars / len(original_text)) * 100
    return accuracy

def calculate_wpm(total_chars, time_taken):
    # Assuming an average word length of 5 characters
    avg_word_length = 5
    words_typed = total_chars / avg_word_length
    minutes_taken = time_taken / 60
    wpm = words_typed / minutes_taken
    return wpm

def typing_speed_test():
    print("Welcome to Typing Speed Tester!")
    print("Type the following text. Press Enter when done.")
    
    text_to_type = get_random_text()
    print(text_to_type)
    
    input("Press Enter to start typing...")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()
    
    # Calculate the time taken and total characters typed
    time_taken = end_time - start_time
    total_chars_typed = len(user_input)
    
    # Calculate WPM and accuracy
    wpm = calculate_wpm(total_chars_typed, time_taken)
    accuracy = calculate_accuracy(text_to_type, user_input)
    
    print("\nTest Result:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Total characters typed: {total_chars_typed}")
    print(f"Your typing speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_speed_test()

