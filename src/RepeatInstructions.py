# LLMs tend not to process the metaprompt attributing the same weight or imprortance to all the sections.
# But by repeating the main instruction at the end of the prompt can help the model overcome its inner recency bias.

# Recency bias is the tendency of LLMs to give more weight to the information that appears
# near the end of a prompt, and ignore or forget the information that appears earlier. This
# can lead to inaccurate or inconsistent responses that do not take into account the whole
# context of the task. For example, if the prompt is a long conversation between two people,
# the model may only focus on the last few messages and disregard the previous ones.

import os
import openai

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"), 
)

conversation = """
[Setting: A sunny park with a bench under a tree]

Emma: [smiling] "Wow, what a beautiful day! The weather is perfect—warm sun, cool breeze. It feels like the universe is giving us a big hug!"

Liam: [grinning] "I know, right? Days like this remind me why I love coming outside. Plus, spending it with my favorite person? Double the good vibes!"

Emma: [laughs] "Flattery will get you everywhere, Liam. But seriously, it feels so nice to take a break. Work's been hectic lately, but this is exactly what I needed."

Liam: "You deserve it, Emma. You’ve been working so hard. It’s inspiring, honestly. You know what they say—hard work pays off, and I can see it paying off for you."

Emma: "Thanks, Liam. That really means a lot. And hey, don’t sell yourself short! You’ve been absolutely crushing it with your new project. I can’t wait to see what you create next."

Liam: [shrugs with a grin] "Well, I’ve got a lot of ideas, but I think they’ll really come together. Your support means everything—it’s like having a personal cheerleader, but cooler."

Emma: [playfully] "Oh, I’m cooler than a cheerleader now? That’s a high bar!"

Liam: [chuckling] "Definitely. You’re the MVP of the team. Hey, speaking of cheerleaders, how about celebrating this amazing day with some ice cream? My treat."

Emma: [claps hands excitedly] "You read my mind! Let’s go! And Liam? Thanks for making this day even better."

Liam: "Anytime, Emma. Let’s make this a tradition—sunny days and ice cream with the best company. Life doesn’t get much better than this."

[They both laugh and walk off towards the ice cream stand, chatting happily.]
"""

# Here we are reapeating our instruction at the end again
system_message = f"""
You are a sentiment analyzer. You classify conversations into three categories:
positive, negative, or neutral.
Return only the sentiment, in lowercase and without punctuation.
Conversation:
{conversation}
Remember to return only the sentiment, in lowercase and without punctuation

"""


def main():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": system_message}]
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()