import os
from datetime import datetime

name = os.getenv("WHO_TO_GREET", "World")
print(f"Hello {name}!")
print("This program is running inside GitHub Actions.")
print(f"Current date and time: {datetime.now()}")
