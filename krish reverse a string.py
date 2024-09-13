#### 13th Sep  ## not my solution, practice again


## How do you reverse a string in Python?

def reverse_string(s):
    return s[::-1]



# Slicing (s[::-1]): The slicing operation [::-1] is the key here.

# This slice notation has three components:   start:stop:step.

# Start: Not specified, so it defaults to the beginning of the string.

# Stop: Not specified, so it defaults to the end of the string.

# Step (-1): The -1 step indicates that Python should iterate through the string from right to left ,
                    # effectively reversing it.

# In simple terms, [::-1] means: "start from the end of the string and move backwards until the beginning."