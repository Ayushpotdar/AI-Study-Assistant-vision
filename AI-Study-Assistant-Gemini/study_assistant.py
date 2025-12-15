import sys
from google import genai
from google.genai.errors import APIError 


API_KEY = "AIzaSyCHnaORdwYL5mxUKu2Jmt0GojqEoRUsKDQ" # gemini api key section (no api key pre applied due to security reasons)
MODEL_ID = "gemini-2.5-flash" # The currently used model

if API_KEY == "API KEY HERE":
    print("\n ERROR: Please enter your actual Gemini API key.")
    sys.exit(1)

try:

    client = genai.Client(api_key=API_KEY) # request goes to the client   
    
except Exception as e:
    print("ERROR: Could not recognise the Gemini Client.")
    print(f"Details: {e}")
    sys.exit(1)


print("\n\n      AI Study Assistant-Gemini")
print("         I AM HERE TO ASSIST YOU.")
print("     Type 'exit','stop', to quit.")
print("-" * 150)

##################################################### MAIN LOGIC STARTS HERE ####################################
def run_assistant():
    """Runs the study assistant logic."""
    try:
        study_text = input("Enter your Questions here :-\n") # to take input from the user/student

        if study_text.lower().strip() in ["exit","stop","quit"]:
            print("Always their for you ,","Goodbye!")
            return

        print("\n⏳ Generating Answer and questions for you...") # to print generating statement for user
        
        prompt_explanation = f"""
You are an AI tutor.
Tasks:
1. Explain the given study material in very simple words.
2. Generate exactly 5 conceptual questions based on it.

Study Material:
{study_text}
"""
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt_explanation
        )

        print("\n------Explanation & Questions ------\n")
        print(response.text)
        print("\n" + "-" * 34 + "\n")

        ############### Answer Evaluation ##########################
        print("Now, answer the 5 questions in short.")
        user_answers = input("Enter your 5 answers (separated by commas):\n")

        print("\n⏳ Evaluating answers please wait...")

        evaluation_prompt = f"""
You are an evaluator.
Study Material: {study_text}
Student Answers: {user_answers}

Give brief, constructive feedback on the answers provided. Correct any incorrect answers.
"""
        
        evaluation = client.models.generate_content(
            model=MODEL_ID,
            contents=evaluation_prompt
        )

        print("\n--- AI Feedback ---\n")
        print(evaluation.text)
        print("\n" + "-" * 17 + "\n")

    except APIError as e:
        print(f"\nAPI Error Occurred: {e}")
        print("Check if your API key is valid and if you have quota.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

run_assistant()


