"""Advanced Task 3: Clean Message Toolkit
- Collect a message that might contain extra spaces or mixed casing.
- Use at least three different string methods (e.g. strip, title, replace, upper) to tidy the message.
- Print the original and cleaned versions so the difference is obvious.
- Extension: show the message length before and after cleaning.
"""

raw_message = input("Type a message to tidy: ")
raw_message_length = len(raw_message)

lowered_message = raw_message.lower()
word = lowered_message.split()
cleaned_message = " ".join(word)
final_message = cleaned_message[0].upper() + cleaned_message[1:]
final_message_length = len(final_message)

print(f"Original message: {raw_message}")
print(f"Final message: {final_message}")
print(f"Original message length: {raw_message_length}")
print(f"Final message length: {final_message_length}")
# TODO: apply a sequence of string methods to produce a cleaned_message
# Example methods: strip, title, replace, lower, upper
# TODO: display the original and cleaned messages
# Extension: display the character counts for each version
