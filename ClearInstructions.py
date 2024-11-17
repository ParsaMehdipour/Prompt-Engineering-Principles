# The principle of giving clear instructions is to provide the model with enough information and guidance
# to perform the task correctly and efficiently. Defeine the following details in your prompts:
# 1.The goal or objective of the task.
# 2.The format or structure of the expected output.
# 3.The constraints or limitations of the task.
# 4.The context or background of the task.

import os
import openai

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"), 
)

system_message = """
You are an AI assistant that helps humans by generating tutorials given a
text.
You will be provided with a text. If the text contains any kind of
istructions on how to proceed with something, generate a tutorial in a
bullet list.
Otherwise, inform the user that the text does not contain any
instructions.
Text:
"""

instructions = """
To prepare the known sauce from Genova, Italy, you can start by toasting
the pine nuts to then coarsely
chop them in a kitchen mortar together with basil and garlic. Then, add
half of the oil in the kitchen mortar and season with salt and pepper.
Finally, transfer the pesto to a bowl and stir in the grated Parmesan
cheese.
"""

def main():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": system_message}, {"role": "user", "content": instructions}]
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()