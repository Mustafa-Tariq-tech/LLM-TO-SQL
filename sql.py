from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os 
import sqlite3
import google.generativeai as genai

## configure GEnai key

genai.configure(api_key=(os.getenv("gemini_api_key")))


def gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    
    response=model.generate_content([prompt,question])
  
    return response.text


def read_sql_query(sql,db):

    conn=sqlite3.connect(db)
    
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
   

    
    return rows


prompt = """
Your an expert in converting English to SQL query!
The SQL database has the name STUDENT and has the following columns -
NAME, CLASS, SECTION.

For example:
Example 1 - How many entries of records are present?
The SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;
Also, the SQL code should not have ''' in the beginning or end and SQL word in output.

Example 2 - How many students study Data Science in class?
The SQL command will be something like this: SELECT * FROM STUDENT WHERE CLASS="Data Science";
Also, the SQL code should not have ''' in the beginning or end and SQL word in output.
"""

st.set_page_config(page_title="I can retrieve Any SQL query")
st.header("Gemini APP to Retrive ")

question=st.text_input("input",key="input")
submit=st.button("ask the Question")
#submit clicked
if submit:
    response1=gemini_response(question,prompt)
  
    response=read_sql_query(response1,"student.db")
   
    st.header("The Response is")
    for row in response:
        print(row)
        st.header(row)
    st.write("query used is :",response1)





    



