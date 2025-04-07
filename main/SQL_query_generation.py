import openai
from django.conf import settings
from .databasecontext import db_context
import os 
import json
import logging
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
        print(sql_query, flush=True)
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
                    "content": f"The user asked this question: '{question}'. The answer to the question is: {results}. Please respond to the user with a full sentence using the result. If the result is None, say 'sorry, we couldn't find what you were looking for. Please try another search'"
                },
            ],
            temperature=0.2,
            max_tokens=1024
        )

        user_results = response['choices'][0]['message']['content'].strip()        

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are generating a python dictionary to be passed into a function , with key's using double quoted strings instead of single quotes. Only include the python dictionary with NO ADDITIONAL CHARACTERS. Please assign keys and values to mimic a sql query result"
                },
                {
                    "role": "system",
                    "content": f"create this sentence into a python dictionary DO NOT CREATE A DICTIONARY OF DICTIONARIES OR A LIST OF DICTIONARIES, {user_results}"
                },
                {
                    "role": "system",
                    "content": """Desired Output Example: {"Player": "Aaron Rodgers", "Year": 2011, "Passing Yards": 4643, "Completion Rate": 68.3, "Passer Rating": 122.5}"""
                }
            ],
            temperature=0.2,
            max_tokens=1024
        )
        table_results = response['choices'][0]['message']['content'].strip()

        
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
    
def clean_python_table(table):

    if table is None:
        return None
    #print(table)
    if table.startswith("```python") and table.endswith("```"):
        # Remove the starting '```sql' and ending '```'
        cleaned_table = table[9:-3].strip()  # 9 is the length of '```python' and 3 is for closing '```'

        #Check for double quotes
        cleaned_table = cleaned_table.replace("'", '"')
        print(cleaned_table)
        payload = json.loads(cleaned_table)
        print("table_result_type",type(payload))
        print(payload)
        return payload
    else:
        # Return the table as is if it doesn't start with '```sql' or ends with '```'
        payload = table.replace("'", '"')
        print(payload)
        payload = json.loads(table)
        print("table_result_type",type(payload))
        print(payload)
        return payload
