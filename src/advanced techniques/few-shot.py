# This is an example and evidence of how the concept of few-shot learning – which means providing
# the model with examples of how we would like it to respond – is a powerful technique that enables
# model customization without interfering with the overall architecture.

import os
import openai

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"), 
)

system_message = """
You are an AI marketing assistant. You help users to create taglines for new
product names.
Given a product name, produce a tagline similar to the following examples:

Peak Pursuit - Conquer Heights with Comfort
Summit Steps - Your Partner for Every Ascent
Crag Conquerors - Step Up, Stand Tall

Product name:

"""

product_name = 'Elevation Embrace'

def main():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": system_message}, {"role": "user", "content": product_name}]
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()