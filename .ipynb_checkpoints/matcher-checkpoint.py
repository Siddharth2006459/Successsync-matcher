def calculate_match_score(user1, user2):
    score = 0

    if user1['vision'] == user2['vision']:
        score += 30
    if user1['skills'] & user2['skills']:
        score += 25
    if user1['mindset'] == user2['mindset']:
        score += 20
    if abs(user1['hours'] - user2['hours']) <= 2:
        score += 15
    if user1['risk'] == user2['risk']:
        score += 10

    return score

# Example usage
userA = {
    'vision': 'AI for Education',
    'skills': {'Python', 'ML'},
    'mindset': 'Growth',
    'hours': 5,
    'risk': 'High'
}

userB = {
    'vision': 'AI for Education',
    'skills': {'Python', 'Web'},
    'mindset': 'Growth',
    'hours': 6,
    'risk': 'High'
}

print("Match Score:", calculate_match_score(userA, userB))
