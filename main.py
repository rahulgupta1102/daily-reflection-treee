def calculate_score(mood, productivity, stress):
    score = 0

    # Mood scoring
    if mood == "good":
        score += 2
    elif mood == "neutral":
        score += 1
    elif mood == "bad":
        score -= 2

    # Productivity scoring
    if productivity == "high":
        score += 2
    elif productivity == "medium":
        score += 1
    elif productivity == "low":
        score -= 1

    # Stress scoring
    if stress == "high":
        score -= 2
    elif stress == "low":
        score += 1

    return score


def get_feedback(score):
    if score >= 4:
        return "Excellent day! Keep maintaining this balance."
    elif score >= 1:
        return "Good day, but there is room for improvement."
    elif score >= -1:
        return "Average day. Try to improve your focus and reduce stress."
    else:
        return "Tough day. Take rest and reflect on improvements."


def daily_reflection(mood, productivity, stress):
    score = calculate_score(mood, productivity, stress)
    feedback = get_feedback(score)

    return {
        "score": score,
        "feedback": feedback
    }


# Example run
result = daily_reflection("bad", "low", "high")

print("Score:", result["score"])
print("Feedback:", result["feedback"])