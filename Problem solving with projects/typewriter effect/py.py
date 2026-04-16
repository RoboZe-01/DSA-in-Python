import time
import sys

def typewriter_effect(text, delay=0.1):
    for char in text:
        # sys.stdout.write ensures it prints without adding a new line
        sys.stdout.write(char)
        # flush ensures the character appears immediately
        sys.stdout.flush()
        # Sleep for the duration of the delay
        time.sleep(delay)
    # Print a new line at the very end
    print()

# Example usage
typewriter_effect("Welcome to the event! Please check your access status.")