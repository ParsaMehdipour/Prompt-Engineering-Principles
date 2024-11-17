# Delimiters help our LLM to better understand its intents as well as relate different sections and paragraphs to each other.
# we can use delimiters within our prompt. A delimiter can be any sequence of characters
# or symbols that is clearly mapping a schema rather than a concept. For example, we can consider
# the following sequences to be delimiters:
#  >>>>
#  ====
#  ------
#  ####
#  ` ` ` ` `

import os
import openai

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"), 
)

system_message = """
You are a Python expert who produces Python code as per the user's request.

===>START EXAMPLE

---User Query---
Give me a function to print a string of text.

---User Output---
Below you can find the described function:
```def my_print(text):
    return print(text)
```
<===END EXAMPLE

"""

query = "generate a Python function to calculate the nth Fibonacci number"

def main():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": system_message}, {"role": "user", "content": query},]
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()