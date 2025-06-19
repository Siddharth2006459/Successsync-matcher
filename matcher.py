import numpy as np
import ast
from models import session, User

def cosine_similarity(vec1, vec2):
    """Compute cosine similarity between two vectors."""
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def get_top_matches(current_user, top_k=5):
    """Return the top K matching users based on vision embedding similarity."""
    try:
        current_vec = np.array(ast.literal_eval(current_user.embedding))
    except:
        return []

    users = session.query(User).filter(User.id != current_user.id).all()
    results = []

    for user in users:
        try:
            other_vec = np.array(ast.literal_eval(user.embedding))
            sim = cosine_similarity(current_vec, other_vec)
            results.append((user.name, round(sim * 100, 2)))
        except:
            continue

    results.sort(key=lambda x: x[1], reverse=True)
    return results[:top_k]
