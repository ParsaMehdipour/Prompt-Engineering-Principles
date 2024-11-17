# Sometimes, the tasks are too complex or ambiguous for a single prompt
# to handle, and it is better to split them into simpler subtasks that can be solved by different prompts.

import os
import openai

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"), 
)

system_message = """
You are an AI assistant that summarizes articles.
To complete this task, do the following subtasks:
Read the provided article context comprehensively and identify the main
topic and key points
Generate a paragraph summary of the current article context that captures
the essential information and conveys the main idea
Print each step of the process.
Article:
"""

instructions = """
Recurrent Neural Networks and Long Short-Term Memory: A Deep Dive

Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) networks are integral components of deep learning, widely used for sequence data processing. From text and speech recognition to time-series forecasting, these models shine when handling data where temporal or sequential order matters.

What are Recurrent Neural Networks?
RNNs are a class of artificial neural networks designed to recognize patterns in sequences of data. Unlike traditional feedforward networks, RNNs have loops that allow information to persist over time. This characteristic makes them suitable for tasks where context and previous inputs influence the current output.

In an RNN, the hidden state at each time step serves as a memory, capturing information about previous inputs in the sequence. This architecture enables RNNs to process variable-length input sequences, making them ideal for applications like:

Natural Language Processing (NLP)
Speech-to-text conversion
Financial time-series analysis
However, RNNs suffer from challenges like the vanishing gradient problem, where gradients diminish as they backpropagate through time. This issue hampers learning long-term dependencies in sequences, limiting the model's effectiveness for tasks involving extended contexts.

Long Short-Term Memory Networks
To address the limitations of standard RNNs, Long Short-Term Memory (LSTM) networks were introduced by Hochreiter and Schmidhuber in 1997. LSTMs are a special kind of RNN capable of learning long-term dependencies. They achieve this through a unique architecture that employs "gates" to control the flow of information.
"""

def main():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": system_message}, {"role": "user", "content": instructions}]
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()