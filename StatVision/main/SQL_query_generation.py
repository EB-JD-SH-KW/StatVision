import openai
from django.conf import settings
from .databasecontext import db_context

# Set your OpenAI API key (using the key stored in settings)
#openai.api_key = settings.OPENAI_API_KEY
openai.api_key = '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'


def generate_sql_query(english_query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are in a web app to translate user input into SQL queries. Your response should contain nothing but the query. Please make the query one line on text and use mySQL syntax Format columns using backticks (`) not quotes, for the table names do not put any quotes or backticks. The current year is 2025"},
                {"role": "system", "content": db_context},
                {"role": "user", "content": f"Translate this English query into an SQL query: {english_query}"}
            ],
            temperature=0.2,
            max_tokens=1024  # Lowered for safety; adjust as needed
        )

        sql_query = response['choices'][0]['message']['content'].strip()

        # ✅ Show token usage
        print("Token usage:", response['usage'])

        return sql_query

    except Exception as e:
        print(f"Error generating SQL query: {e}")
        return None
