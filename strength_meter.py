import re

def evaluate_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r'[A-Z]', password): score += 1
    if re.search(r'[a-z]', password): score += 1
    if re.search(r'\d', password): score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): score += 1
    labels = ['Very Weak', 'Weak', 'Fair', 'Good', 'Strong', 'Very Strong']
    return score, labels[score]
