import json

def parse_user_input(user_query):
    user_query=user_query.lower()
    result = {
        'task':'forcast',
        'horizon': 10
    }

    words = user_query.split()
    for word in words:
        if word.isdigit():
            result['horizon'] = int(word)
    
    return result