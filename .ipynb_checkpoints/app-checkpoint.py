import os
from dotenv import load_dotenv
import openai
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

import openai
from dotenv import load_dotenv
import os
def get_embedding(text):
    response = openai.Embedding.create(
        model="text-embedding-ada-002",  # This is OpenAI's powerful vision-understanding model
        input=text
    )
    return response['data'][0]['embedding']
import numpy as np

def get_embedding(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-3-small"  # lightweight and great for short text
    )
    return response['data'][0]['embedding']

# Load your API key from .env
load_dotenv('u.env')
openai.api_key = os.getenv("OPENAI_API_KEY")

from matcher import get_top_matches
import streamlit as st
from models import session, User
def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

st.title("🚀 SuccessSync Co-Founder Matcher")

# --- INPUT FIELDS ---
name = st.text_input("Your Name")
vision = st.text_input("Vision")
skills = st.multiselect("Skills", ["Python", "Web", "ML", "AI", "Design", "Leadership"])
mindset = st.selectbox("Mindset", ["Growth", "Fixed"])
hours = st.slider("How many hours/day can you work?", 1, 12)
risk = st.selectbox("Risk Appetite", ["High", "Medium", "Low"])

submit = st.button("Submit")

if submit:
    embedding = get_embedding(vision)

    new_user = User(
        name=name,
        vision=vision,
        skills=",".join(skills),
        mindset=mindset,
        hours=hours,
        risk=risk,
        embedding=",".join(map(str, embedding))
    )

    session.add(new_user)
    session.commit()
    st.success("🎉 Your profile has been saved!")
    st.subheader("🔍 Your Top Matches")
    matches = get_top_matches(new_user)

    if matches:
        for name, score in matches:
            st.write(f"✅ {name} — Match Score: {score}")
    else:
        st.write("❌ No matches found yet. Please try again later!")
        def get_vision_similarity(vision1, vision2):
          response = openai.Embedding.create(
        input=[vision1, vision2],
        model="text-embedding-ada-002"
    )
    vec1 = response["data"][0]["embedding"]
    vec2 = response["data"][1]["embedding"]
    
         similarity = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return round(similarity * 100, 2)
    except Exception as e:
        st.error(f"OpenAI API Error: {e}")
        return 0


