import openai
from django.conf import settings
from .databasecontext import db_context
import os
from dotenv import load_dotenv



load_dotenv()
api_key = os.getenv("OPEN_AI_KEY")
openai.api_key = api_key


def generate_sql_query(english_query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are in a web app to translate user input into SQL queries. Your response should contain nothing but the query. Please make the query one line of text and use mySQL syntax Format columns using backticks (`) not quotes, for the table names do not put any quotes or backticks. The current year is 2025"},
                {"role": "system", "content": db_context},
                {"role": "user", "content": f"Translate this English query into an SQL query: {english_query}"}
            ],
            temperature=0.2,
            max_tokens=1024  # Lowered for safety; adjust as needed
        )

        sql_query = response['choices'][0]['message']['content'].strip()

        #show token usage
        print("Token usage:", response['usage'])

        return sql_query

    except Exception as e:
        print(f"Error generating SQL query: {e}")
        return None

def generate_users_results(question, results):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are generating a response from an SQL query to a user."
                },
                {
                    "role": "system",
                    "content": f"The user asked this question: '{question}'. The answer to the question is: {results}. Please respond to the user with a full sentence using the result."
                },
            ],
            temperature=0.2,
            max_tokens=1024
        )

        user_results = response['choices'][0]['message']['content'].strip()        
        print("Token usage:", response['usage'])

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are generating a python dictionary to be passed into a function, only include the python dictionary with NO ADDITIONAL CHARACTERS"
                },
                {
                    "role": "system",
                    "content": f"create this sentence into a list of dictionaries to use in python, {user_results}"
                },
            ],
            temperature=0.2,
            max_tokens=1024
        )
        table_results = response['choices'][0]['message']['content'].strip()

        
        print("Token usage:", response['usage'])
        return user_results, table_results
    
    except Exception as e:
        print(f"Error generating response: {e}")
        return None


def clean_sql_query(query):
    # Check if the query starts with '```sql' and ends with '```'
    if query is None:
        return None
    
    if query.startswith("```sql") and query.endswith("```"):
        # Remove the starting '```sql' and ending '```'
        cleaned_query = query[6:-3].strip()  # 6 is the length of '```sql' and 3 is for closing '```'
        return cleaned_query
    else:
        # Return the query as is if it doesn't start with '```sql' or ends with '```'
        return query
    
def clean_python_table(query):
    # Check if the query starts with '```sql' and ends with '```'
    if query is None:
        return None
    
    if query.startswith("```python") and query.endswith("```"):
        # Remove the starting '```sql' and ending '```'
        cleaned_query = query[9:-3].strip()  # 6 is the length of '```sql' and 3 is for closing '```'
        return cleaned_query
    else:
        # Return the query as is if it doesn't start with '```sql' or ends with '```'
        return query
