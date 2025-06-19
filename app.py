import os
import numpy as np
import streamlit as st
from sentence_transformers import SentenceTransformer
from matcher import get_top_matches
from models import session, User

# ✅ Load the local transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ Streamlit App UI
st.title("🚀 SuccessSync Co-Founder Matcher")

# --- Input Fields ---
name = st.text_input("Your Name", key="name_input")
vision = st.text_input("Vision", key="vision_input")
skills = st.multiselect("Skills", ["Python", "Web", "ML", "AI", "Design", "Leadership"], key="skills_input")
mindset = st.selectbox("Mindset", ["Growth", "Fixed"], key="mindset_input")
hours = st.slider("How many hours/day can you work?", 1, 12, key="hours_input")
risk = st.selectbox("Risk Appetite", ["High", "Medium", "Low"], key="risk_input")

submit = st.button("Submit", key="submit_button")

# ✅ Local embedding function
def get_embedding(text):
    try:
        return model.encode(text).tolist()
    except Exception as e:
        st.error(f"❌ Local embedding error: {e}")
        return None

# ✅ Cosine similarity helper (used by matcher.py if needed)
def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# ✅ Main logic
if submit:
    embedding = get_embedding(vision)

    if embedding is None:
        st.error("❌ Failed to create embedding. Try different input.")
    else:
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
            for match_name, score in matches:
                st.write(f"✅ {match_name} — Match Score: {score}")
        else:
            st.write("❌ No matches found yet.")
