import streamlit as st
import pandas as pd
import google.generativeai as genai

st.title("Chatbot with Dataset")

data = pd.read_csv(r"C:\Users\Arun Kumaran\Desktop\Renewable_Energy_Forecasting.csv") 

context = f"**Dataset Description:**\n\n"
context += f"This dataset contains {data.shape[0]} rows and {data.shape[1]} columns.\n"
context += "Column names: " + ", ".join(data.columns) + "\n\n"
context += "**Sample Data:**\n" 
context += data.to_markdown(index=False)

api_key = 'api_key' 
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_content(prompt):

  try:
    response = model.generate_content([prompt])
    return response.text if response else "Error: No response received."
  except Exception as e:
    return f"An error occurred: {str(e)}"

st.write("Ask any question about the dataset:")
user_question = st.text_input("Ask me anything:")

if st.button("Get Answer"):
  if user_question:
    full_prompt = f"{context}\n\n**Question:** {user_question}"
    answer = generate_content(full_prompt)
    st.write(f"Answer: {answer}")
  else:
    st.write("Please enter a question to get an answer.")
