import sys
import time

def loading_animation():
    """Simulate a loading animation."""
    print("Loading", end="")
    for _ in range(5):  # Print dots with a delay
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.5)  # Wait for 0.5 seconds between each dot
    print("\nGame Loaded!")
