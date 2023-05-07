import re

def searchInList(listOfSearch, text):
    matchF = ''
    match_text = ''
    text = text.replace('\n', ' ')
    for searchTerm in listOfSearch:
        escapedTerm = re.escape(searchTerm)
        match = re.search(escapedTerm, text, re.IGNORECASE)
        if match:
            matchF = str(searchTerm)
            start = max(0, match.start() - 20)
            end = min(len(text), match.end() + 20)
            prefix = '(...) ' if start > 0 else ''
            suffix = ' (...)' if end < len(text) else ''
            match_text = f"{prefix}{text[start:end]}{suffix}"
            break

    return matchF, match_text