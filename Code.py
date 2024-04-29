import os
import streamlit as st
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# Title for the Streamlit app
st.title("NL to SQL Converter")
# Text input for user's natural language query
user_input = st.text_input("Enter a natural language query:")
# Button to trigger the conversion
if st.button("Convert to SQL"):
if user_input:
# Send the user's input to OpenAI's GPT-4
response = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[{"role": "system", "content": "You are a helpful assistant that translates NL to SQL."},
{"role": "user", "content": user_input}],
temperature=0.7,
23
max_tokens=100,
)
# Extract and display the SQL response from OpenAI
sql_response = response["choices"][0]["message"]["content"]
st.write("SQL Query:")
st.code(sql_response, language="sql")
# Add instructions or a brief explanation
st.markdown("Enter a natural language query, and this app will convert it into an SQL query.")
