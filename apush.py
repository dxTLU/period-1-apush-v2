QUESTIONS = [
    {
        "year": 1492,
        "question": "Which development most directly resulted from sustained contact after 1492?",
        "choices": [
            "The Columbian Exchange of plants, animals, people, and diseases",
            "The immediate abolition of European empires",
            "The end of Atlantic trade",
            "The disappearance of Indigenous political systems",
        ],
        "answer": 1,
        "explanation": "The Columbian Exchange transferred organisms and people among the Americas, Europe, and Africa."
    },
    {
        "year": 1500,
        "question": "Which factor best explains why European conquest could disrupt large Indigenous states so rapidly?",
        "choices": [
            "Indigenous societies had no political organization",
            "European alliances, military technologies, and epidemic disease interacted with existing rivalries",
            "Europeans had overwhelming population numbers in the Americas",
            "All Indigenous groups supported Spanish rule",
        ],
        "answer": 2,
        "explanation": "Conquest resulted from interacting factors, including Indigenous political divisions, alliances, European military advantages, and epidemic disease."
    },
    {
        "year": 1512,
        "question": "The Laws of Burgos are most directly associated with which broader issue?",
        "choices": [
            "Debates over Indigenous labor and Spanish colonial governance",
            "The creation of the United States Constitution",
            "The abolition of European monarchy",
            "The end of Christian missionary activity",
        ],
        "answer": 1,
        "explanation": "Spanish authorities attempted to regulate colonial labor and Indigenous treatment while maintaining imperial and missionary goals."
    },
    {
        "year": 1519,
        "question": "Which concept is most useful for explaining why Cortés gained Indigenous allies?",
        "choices": [
            "Continuity and change in local political rivalries",
            "Isolation from Indigenous politics",
            "The absence of centralized states",
            "Industrialization",
        ],
        "answer": 1,
        "explanation": "Existing rivalries within the Mexica political sphere shaped the alliances available to Spanish forces."
    },
]

def ask_question(state, year):
    available = [q for q in QUESTIONS if q["year"] == year]
    if not available:
        return
    q = available[0]
    print("\n" + "=" * 60)
    print("APUSH CHECK")
    print(q["question"])
    for i, choice in enumerate(q["choices"], 1):
        print(f"{i}. {choice}")
    while True:
        raw = input("> ").strip()
        try:
            answer = int(raw)
            if 1 <= answer <= len(q["choices"]):
                break
        except ValueError:
            pass
        print("Enter a valid answer.")
    if answer == q["answer"]:
        state.apush_score += 1
        print("Correct.")
    else:
        print(f"Not quite. Correct answer: {q['answer']}.")
    print(q["explanation"])
    input("\nPress ENTER to continue...")
