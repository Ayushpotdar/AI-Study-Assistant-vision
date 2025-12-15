# AI Study Assistant (Powered by Google Gemini API)

## Problem Statement
Students often struggle to understand complex study material and lack immediate feedback on their learning. 
Traditional learning methods do not adapt to the learner’s pace or understanding level.

## Solution
The AI Study Assistant is a text-based learning tool that uses Google’s Gemini API to:
- Explain study topics in very simple language
- Automatically generate conceptual questions
- Evaluate student answers and provide constructive feedback

This helps learners understand topics better and test their knowledge instantly.

---

## How Gemini API is Used (Core Feature)
The Gemini API is the **core intelligence** of this application.

It is used to:
1. Reason over user-provided study material
2. Generate simplified explanations
3. Create exactly 5 conceptual questions
4. Evaluate answers with feedback using minimal API calls

Prompt engineering is used to clearly instruct Gemini on each task, ensuring accurate and consistent responses.

---

## Tech Stack
- Programming Language: **Python 3**
- AI Model: **Google Gemini (gemini-2.5-flash)**
- Library: **google-generativeai / google-genai**
- Platform: **Command Line Interface (CLI)**

---

## How to Run the Project

### Step 1: Install Python Dependencies
```bash
pip install google-genai
