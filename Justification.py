# LLMs are built in such a way that they predict the next token based on the previous ones without
# looking back at their generations. This might lead the model to output wrong content to the user, yet
# in a very convincing way. If the LLM-powered application does not provide a specific reference to
# that response, it might be hard to validate the ground truth behind it. Henceforth, specifying in the
# prompt to support the LLM’s answer with some reflections and justification could prompt the model to
# recover from its actions. Furthermore, asking for justification might be useful also in case of answers
# that are right but we simply don’t know the LLM’s reasoning behind it.

import os
import openai

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"), 
)

system_message = """
You are an AI assistant specialized in solving riddles.
Given a riddle, solve it the best you can.
Provide a clear justification of your answer and the reasoning behind it.
Riddle:

"""

instructions = """
What has a face and two hands, but no arms or legs?
"""

def main():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": system_message}, {"role": "user", "content": instructions}]
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()