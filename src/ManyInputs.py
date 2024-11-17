# LLMs are built in such a way that they predict the next token based
# on the previous ones without looking back at their generations. If this is the case, if one sampled token
# is the wrong one (in other words, if the model is unlucky), the LLM will keep generating wrong tokens
# and, henceforth, wrong content. Now, the bad news is that, unlike humans, LLMs cannot recover
# from errors on their own. This means that, if we ask them, they acknowledge the error, but we need
# to explicitly prompt them to think about that.
# One way to overcome this limitation is to broaden the space of probabilities of picking the right token.
# Rather than generating just one response, we can prompt the model to generate multiple responses,
# and then pick the one that is most suitable for the user’s query. This splits the job into two subtasks
# for our LLM:
# 1. Generating multiple responses to the user’s query
# 2. Comparing those responses and picking the best one, according to some criteria we can specify
# in the metaprompt

import os
import openai

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"), 
)

# Justifications and
system_message = """
You are an AI assistant specialized in solving riddles.
Given a riddle, you have to generate three answers to the riddle.
For each answer, be specific about the reasoning you made.
Then, among the three answers, select the one that is most plausible given the
riddle.
Riddle:

"""

riddle = """
What has a face and two hands, but no arms or legs?
"""

def main():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": system_message}, {"role": "user", "content": riddle}]
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()