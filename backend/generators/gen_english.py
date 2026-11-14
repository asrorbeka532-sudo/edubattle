import random
from common import make_q, insert_questions

def generate_english_questions():
    questions = []

    # 1. English Tenses (120 questions)
    tenses_qs = [
        ("Water ______ at 100 degrees Celsius.", "boils", ["is boiling", "boiled", "will boil"], "Scientific facts and general truths take the Present Simple tense ('boils')."),
        ("Look at those dark clouds! It ______ rain.", "is going to", ["will", "is raining", "was"], "Predictions based on present evidence take 'be going to'."),
        ("She ______ English for five years now.", "has been learning", ["learns", "is learning", "learned"], "Actions that started in the past and continue up to now take Present Perfect Continuous."),
        ("When I arrived at the cinema, the movie ______ already started.", "had", ["has", "was", "would"], "Past Perfect is used for an action that happened before another action in the past."),
        ("Listen! Someone ______ the piano upstairs.", "is playing", ["plays", "played", "has played"], "Actions happening right at the moment of speech ('Listen!') take Present Continuous."),
        ("Yesterday at 8 PM, we ______ dinner together.", "were having", ["had", "have", "are having"], "An action in progress at a specific past time takes Past Continuous ('were having')."),
        ("By this time next year, they ______ from university.", "will have graduated", ["will graduate", "are graduating", "graduate"], "Actions completed by a certain future point take Future Perfect ('will have graduated')."),
        ("He usually ______ to school by bus, but today he is walking.", "goes", ["is going", "went", "has gone"], "Habitual routines take Present Simple ('goes').")
    ]
    for _ in range(120):
        t = random.choice(tenses_qs)
        questions.append(make_q(7, "Tenses (Grammar)", t[0], t[1], t[2], t[3], "orta", "8-sinf"))

    # 2. Passive Voice & Reported Speech (100 questions)
    pass_qs = [
        ("The telephone ______ by Alexander Graham Bell in 1876.", "was invented", ["invented", "is invented", "has been invented"], "Past Simple Passive: was/were + V3 ('was invented')."),
        ("Romeo and Juliet ______ by William Shakespeare.", "was written", ["wrote", "is written", "had written"], "Historical creation takes Past Simple Passive ('was written')."),
        ("A new hospital ______ in our city right now.", "is being built", ["is built", "builds", "was built"], "Present Continuous Passive: is/are being + V3 ('is being built')."),
        ("'I am tired,' Tom said. -> Tom said that he ______ tired.", "was", ["is", "had been", "will be"], "In reported speech, Present Simple backshifts to Past Simple ('am' -> 'was')."),
        ("'I will call you tomorrow,' she promised. -> She promised that she ______ call me the next day.", "would", ["will", "can", "had"], "In reported speech, 'will' changes to 'would'."),
        ("Many languages ______ in Europe.", "are spoken", ["speak", "are speaking", "were spoke"], "Present Simple Passive: is/are + V3 ('are spoken').")
    ]
    for _ in range(100):
        t = random.choice(pass_qs)
        questions.append(make_q(7, "Passive Voice & Reported Speech", t[0], t[1], t[2], t[3], "orta", "9-sinf"))

    # 3. Conditionals & Wish Clauses (110 questions)
    cond_qs = [
        ("If it rains tomorrow, we ______ the picnic.", "will cancel", ["cancel", "would cancel", "cancelled"], "First Conditional (real possibility): If + Present Simple, will + V1."),
        ("If I ______ a million dollars, I would travel around the world.", "had", ["have", "will have", "would have"], "Second Conditional (hypothetical present): If + Past Simple, would + V1."),
        ("If she had studied harder, she ______ the exam.", "would have passed", ["will pass", "passed", "would pass"], "Third Conditional (past regret): If + Past Perfect, would have + V3."),
        ("If you heat ice, it ______ into water.", "melts", ["will melt", "melted", "would melt"], "Zero Conditional (general truth/law of nature): If + Present, Present."),
        ("I wish I ______ more free time to read books.", "had", ["have", "will have", "would have"], "Wish about present desire takes Past Simple ('had')."),
        ("She wishes she ______ that expensive dress yesterday.", "hadn't bought", ["didn't buy", "doesn't buy", "won't buy"], "Wish about past regret takes Past Perfect ('hadn't bought').")
    ]
    for _ in range(110):
        t = random.choice(cond_qs)
        questions.append(make_q(7, "Conditionals & Wishes", t[0], t[1], t[2], t[3], "qiyin", "9-sinf"))

    # 4. Modal Verbs (100 questions)
    mod_qs = [
        ("You ______ smoke here; it is strictly prohibited by law.", "mustn't", ["don't have to", "needn't", "should"], "'Mustn't' expresses strong prohibition."),
        ("You ______ bring food; lunch is provided for everyone.", "don't have to (needn't)", ["mustn't", "can't", "shouldn't"], "'Don't have to' / 'needn't' expresses absence of obligation (kerak emas)."),
        ("Look! He has a brand new car and a huge mansion. He ______ be very rich.", "must", ["can't", "might not", "shouldn't"], "'Must' expresses 95%+ logical deduction (shubhasiz, bo'lsa kerak)."),
        ("She hasn't eaten all day. She ______ be very hungry.", "must", ["can't", "needn't", "mustn't"], "Logical deduction based on facts: must be hungry."),
        ("You ______ see a doctor if your headache continues.", "should", ["mustn't", "can't", "needn't"], "'Should' expresses friendly advice or recommendation.")
    ]
    for _ in range(100):
        t = random.choice(mod_qs)
        questions.append(make_q(7, "Modal Verbs", t[0], t[1], t[2], t[3], "orta", "8-sinf"))

    # 5. Gerunds vs Infinitives (100 questions)
    gi_qs = [
        ("I really enjoy ______ to classical music in the evening.", "listening", ["to listen", "listen", "listened"], "'Enjoy' is followed by a gerund (-ing form)."),
        ("They decided ______ a new house in the suburbs.", "to buy", ["buying", "buy", "bought"], "'Decide' is followed by a to-infinitive."),
        ("He avoided ______ eye contact with the interviewer.", "making", ["to make", "make", "made"], "'Avoid' takes gerund (-ing)."),
        ("Don't forget ______ the door when you leave.", "to lock", ["locking", "lock", "locked"], "'Forget to do' means remember to perform a future task."),
        ("I promised ______ her with the homework.", "to help", ["helping", "help", "helped"], "'Promise' takes to-infinitive."),
        ("Would you mind ______ the window? It's hot in here.", "opening", ["to open", "open", "opened"], "'Would you mind' is always followed by V-ing.")
    ]
    for _ in range(100):
        t = random.choice(gi_qs)
        questions.append(make_q(7, "Gerund and Infinitive", t[0], t[1], t[2], t[3], "orta", "9-sinf"))

    # 6. Relative Clauses & Pronouns (100 questions)
    rel_qs = [
        ("The boy ______ won the chess tournament is my classmate.", "who", ["which", "whose", "where"], "We use 'who' for people as subject."),
        ("This is the laptop ______ I bought last week.", "which (that)", ["who", "whose", "where"], "We use 'which' or 'that' for things and objects."),
        ("The teacher ______ car was stolen called the police.", "whose", ["who", "whom", "which"], "'Whose' indicates possession (kimning)."),
        ("Samarkand is the ancient city ______ Amir Temur lived.", "where", ["which", "who", "when"], "'Where' refers to place."),
        ("He cut ______ while slicing the bread.", "himself", ["him", "his", "he"], "Reflexive pronoun for 'he' is 'himself'.")
    ]
    for _ in range(100):
        t = random.choice(rel_qs)
        questions.append(make_q(7, "Relative Clauses", t[0], t[1], t[2], t[3], "orta", "8-sinf"))

    # 7. Prepositions & Dependent Prepositions (110 questions)
    prep_qs = [
        ("She is very good ______ mathematics and chess.", "at", ["in", "on", "with"], "The dependent preposition is 'good at'."),
        ("My brother is interested ______ learning foreign languages.", "in", ["at", "on", "about"], "'Interested in' something."),
        ("They are arriving ______ Tashkent airport ______ 8:30 PM.", "at / at", ["in / on", "on / at", "to / in"], "Arrival at a specific point (airport) at a specific time takes 'at'."),
        ("Our success depends ______ your hard work.", "on", ["in", "at", "of"], "'Depend on' (bog'liq bo'lmoq)."),
        ("Are you afraid ______ spiders?", "of", ["from", "with", "about"], "'Afraid of' (qo'rqmoq)."),
        ("We always celebrate New Year's Eve ______ December 31st.", "on", ["in", "at", "by"], "Specific dates and days take preposition 'on'.")
    ]
    for _ in range(110):
        t = random.choice(prep_qs)
        questions.append(make_q(7, "Prepositions", t[0], t[1], t[2], t[3], "oson", "7-sinf"))

    # 8. Articles & Determiners (110 questions)
    art_qs = [
        ("Tashkent is ______ capital of Uzbekistan.", "the", ["a", "an", "no article (-)"], "Unique specific objects take 'the' ('the capital')."),
        ("He is ______ honest person you can trust.", "an", ["a", "the", "-"], "'Honest' starts with a vowel sound /ɒ/, so it takes 'an'."),
        ("There are only ______ apples left in the basket; we need to buy more.", "a few", ["a little", "much", "many"], "'A few' is used with countable plural nouns for small quantities."),
        ("Do we have ______ sugar in the kitchen?", "any", ["some", "many", "few"], "Questions and negatives with uncountable nouns take 'any'."),
        ("______ Pacific Ocean is the largest ocean on Earth.", "The", ["A", "An", "-"], "Names of oceans, seas, and rivers take the definite article 'the'.")
    ]
    for _ in range(110):
        t = random.choice(art_qs)
        questions.append(make_q(7, "Articles and Determiners", t[0], t[1], t[2], t[3], "oson", "6-sinf"))

    # 9. Adjectives & Comparisons (100 questions)
    adj_qs = [
        ("Mount Everest is ______ mountain in the world.", "the highest", ["higher", "highest", "more high"], "Superlative of one-syllable adjective: the -est ('the highest')."),
        ("Learning Chinese is ______ than learning Spanish.", "more difficult", ["difficultier", "most difficult", "as difficult"], "Comparative of long adjectives: more + adjective + than."),
        ("This is the ______ movie I have ever seen in my life!", "best", ["good", "better", "most good"], "Superlative of irregular adjective 'good' is 'the best'."),
        ("His condition is getting ______ every day.", "worse", ["badder", "worst", "more bad"], "Comparative of irregular adjective 'bad' is 'worse'."),
        ("An elephant is much ______ than a tiger.", "heavier", ["heavy", "heaviest", "more heavy"], "Comparative: -y changes to -ier ('heavier').")
    ]
    for _ in range(100):
        t = random.choice(adj_qs)
        questions.append(make_q(7, "Adjectives & Comparisons", t[0], t[1], t[2], t[3], "oson", "7-sinf"))

    # 10. Phrasal Verbs & Vocabulary (120 questions)
    pv_qs = [
        ("Never ______ your dreams, no matter how hard it gets!", "give up", ["give in", "look up", "take off"], "'Give up' means stop trying or abandon a goal."),
        ("The plane ______ smoothly despite the bad weather.", "took off", ["put on", "took in", "went out"], "'Take off' means leave the ground and begin flight."),
        ("Can you please ______ the light? I want to sleep.", "turn off", ["turn on", "turn into", "turn over"], "'Turn off' means switch off electrical appliance."),
        ("She ______ her mother; they have the same smile and eyes.", "takes after", ["takes over", "looks down", "puts off"], "'Take after' means resemble an older relative."),
        ("They had to ______ the football match due to heavy rain.", "call off (cancel)", ["put on", "call out", "take over"], "'Call off' means cancel an event.")
    ]
    for _ in range(120):
        t = random.choice(pv_qs)
        questions.append(make_q(7, "Phrasal Verbs & Vocabulary", t[0], t[1], t[2], t[3], "orta", "8-sinf"))

    print(f"Generated {len(questions)} English questions.")
    return questions

if __name__ == "__main__":
    qs = generate_english_questions()
    cnt = insert_questions(qs)
    print(f"Successfully inserted {cnt} English questions into database.")
