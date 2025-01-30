# Prompt-Engineering Principles

This repository contains Python scripts demonstrating various **Prompt Engineering** techniques for working with Large Language Models (LLMs). Each script explores a different principle to enhance the effectiveness of AI interactions.

## 📌 Overview
Prompt engineering is a crucial technique in optimizing the performance of LLMs, helping them generate accurate, useful, and context-aware responses. This repository explores several key principles:

### Included Techniques:
1. **Chain of Thought (CoT)** - Encourages step-by-step reasoning to improve complex problem-solving.
2. **Few-Shot Learning** - Provides multiple examples to guide the model’s responses.
3. **Clear Instructions** - Ensures precise guidance to improve output accuracy.
4. **Justification** - Requests explanations to enhance model reliability.
5. **Many Inputs** - Generates multiple responses and selects the best one.
6. **Repeat Instructions** - Mitigates recency bias by reinforcing instructions.
7. **Subtasks** - Breaks down complex tasks into smaller steps.
8. **Delimiters** - Uses structured delimiters for clarity in prompts.

---

## 📂 Files & Descriptions

| File                 | Principle Covered | Description |
|----------------------|------------------|-------------|
| `Chain-of-thought.py` | Chain of Thought | Encourages step-by-step problem-solving for solving first-degree equations. |
| `few-shot.py` | Few-Shot Learning | Demonstrates prompt customization with multiple examples for tagline generation. |
| `ClearInstructions.py` | Clear Instructions | Generates tutorials when given instructional text. |
| `Justification.py` | Justification | Solves riddles while providing reasoning behind answers. |
| `ManyInputs.py` | Many Inputs | Produces multiple responses and selects the best one. |
| `RepeatInstructions.py` | Repeat Instructions | Reinforces key instructions to counteract recency bias. |
| `Subtasks.py` | Subtasks | Breaks down summarization into smaller steps for improved performance. |
| `delimiters.py` | Delimiters | Uses structured formatting for generating Python code snippets. |

---

## 🚀 How to Run
Ensure you have Python installed and set up an OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Then, run any script using:

```bash
python filename.py
```

For example:

```bash
python Chain-of-thought.py
```

---

## 🔥 Why Use These Techniques?
- **Improves accuracy and reasoning** in AI-generated responses.
- **Enhances user interaction** by structuring the AI’s thought process.
- **Minimizes hallucinations** by ensuring the model follows logic.
- **Optimizes LLM responses** for better control and predictability.

---

## 📜 License
This repository is open-source and available under the MIT License.

---

## 📬 Contact
For any queries or contributions, feel free to open an issue or submit a pull request!

---

Happy Prompt Engineering! 🚀

