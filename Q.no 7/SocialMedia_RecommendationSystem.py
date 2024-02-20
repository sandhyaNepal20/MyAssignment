from collections import Counter, defaultdict

# Sample Data (replace with your actual data)
users = {
    1: {"interests": ["music", "comedy"], "neighbors": [2, 3]},
    2: {"interests": ["sports", "comedy"], "neighbors": [1, 4]},
    3: {"interests": ["music", "news"], "neighbors": [1]},
    4: {"interests": ["sports", "tech"], "neighbors": [2]},
}

content = {
    1: {"category": "music", "tags": ["pop", "indie"]},
    2: {"category": "comedy", "tags": ["standup", "satire"]},
    3: {"category": "sports", "tags": ["football", "basketball"]},
    4: {"category": "tech", "tags": ["ai", "gadgets"]},
    5: {"category": "news", "tags": ["politics", "world"]},
}

# Function to combine user interests with neighbor interests
# Function to recommend content based on combined interests
def Sandhya_Recommendation(user_id, n_recommendations=5):
    user_combined_interests = set(users[user_id]["interests"])
    neighbor_interests = set()

    for neighbor in users[user_id]["neighbors"]:
        # interest is list so convert to set
        neighbor_interests.update(users[neighbor]["interests"])

    combined_interests = user_combined_interests.union(neighbor_interests)
    print(f"Combined Interests for user {user_id}: {combined_interests}")

    candidate_scores = defaultdict(float)

    for content_id, content_info in content.items():
        content_tags = set(content_info["tags"])
        common_tags = combined_interests.intersection(content_tags)
        candidate_scores[content_id] = len(common_tags)  # Use the count of common tags as the score

    print(f"Scores for user {user_id}: {candidate_scores}")

    top_recommendations = sorted(candidate_scores, key=candidate_scores.get, reverse=True)[:n_recommendations]
    print(f" Recommendations for user {user_id}: {top_recommendations}")

    return [content[id] for id in top_recommendations]

# Example usage
user_id = 1
recommendations = Sandhya_Recommendation(user_id)
print(f"Recommendations for user {user_id}:")
for item in recommendations:
    print(f"\t- {item['category']}: {item['tags']}")

