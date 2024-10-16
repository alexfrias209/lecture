import ipdb


states_acronyms = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "il",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    # "Kentucky": "KY",
    # "Louisiana": "LA",
    # "Maine": "ME",
    # "Maryland": "MD",
    # "Massachusetts": "MA",
    # "Michigan": "MI",
    # "Minnesota": "MN",
    # "Mississippi": "MS",
    # "Missouri": "MO",
    # "Montana": "MT",
    # "Nebraska": "NE",
    # "Nevada": "NV",
    # "New Hampshire": "NH",
    # "New Jersey": "NJ",
    # "New Mexico": "NM",
    # "New York": "NY",
    # "North Carolina": "NC",
    # "North Dakota": "ND",
    # "Ohio": "OH",
    # "Oklahoma": "OK",
    # "Oregon": "OR",
    # "Pennsylvania": "PA",
    # "Rhode Island": "RI",
    # "South Carolina": "SC",
    # "South Dakota": "SD",
    # "Tennessee": "TN",
    # "Texas": "TX",
    # "Utah": "UT",
    # "Vermont": "VT",
    # "Virginia": "VA",
    # "Washington": "WA",
    # "West Virginia": "WV",
    # "Wisconsin": "WI",
    # "Wyoming": "WY"
}


correct_answers = 0
total_questions = len(states_acronyms)


wrong_answers = {}


for state, acronym in states_acronyms.items():
    condition = False  


    while not condition:
        if state in wrong_answers:
            ipdb.set_trace()
        user_answer = input(f"What is the acronym for {state}? ")

        if user_answer == acronym:
            print("Correct!")
            correct_answers += 1
            condition = True  
            if state in wrong_answers:
                del wrong_answers[state]
        else:
            print(f"Wrong! Try again.")
            wrong_answers[state] = True


print(f"Quiz complete! You got {correct_answers} out of {total_questions} correct.")




