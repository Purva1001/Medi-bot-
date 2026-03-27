import json, os, random
from datetime import datetime

# ---------- KNOWLEDGE BASE ----------
# Each topic has keywords and a response.
# If the user's message contains a keyword, that topic gets picked.

TOPICS = {
    "greeting":  {
        "keywords": ["hello", "hi", "hey"],
        "reply": "Hello! I'm MediBot. Ask me a health question or type 'help'."
    },
    "fever": {
        "keywords": ["fever", "temperature", "chills", "hot"],
        "reply": "Fever tips:\n  - Rest and drink lots of fluids\n  - Cool compress on forehead\n  - Take paracetamol if above 38.5C\n  - See a doctor if it lasts more than 3 days"
    },
    "cough": {
        "keywords": ["cough", "cold", "sore throat", "sneezing", "runny nose"],
        "reply": "Cold & Cough tips:\n  - Drink warm fluids like ginger tea\n  - Steam inhalation helps\n  - Avoid cold drinks\n  - See a doctor if it lasts more than 7 days"
    },
    "headache": {
        "keywords": ["headache", "migraine", "head hurts", "head pain"],
        "reply": "Headache tips:\n  - Drink water first, dehydration is a common cause\n  - Rest in a dark, quiet room\n  - Apply a cold pack to your forehead\n  - See a doctor if headaches happen very often"
    },
    "stomach": {
        "keywords": ["stomach", "nausea", "vomiting", "acidity", "diarrhea", "bloating"],
        "reply": "Stomach tips:\n  - Eat light foods like rice and bananas\n  - Drink ORS if you have diarrhea\n  - Avoid spicy and oily food\n  - See a doctor if pain is severe"
    },
    "diabetes": {
        "keywords": ["diabetes", "sugar", "blood sugar", "insulin", "glucose"],
        "reply": "Diabetes info:\n  - Type 1: body can't make insulin\n  - Type 2: body can't use insulin properly\n  - Eat a balanced diet and exercise regularly\n  - Always follow your doctor's advice"
    },
    "bp": {
        "keywords": ["blood pressure", "bp", "hypertension", "pressure"],
        "reply": "Blood Pressure info:\n  - Normal is 120/80 mmHg\n  - High BP: reduce salt and stress\n  - Low BP: drink more fluids\n  - Only take medicine as prescribed"
    },
    "sleep": {
        "keywords": ["sleep", "insomnia", "tired", "can't sleep", "fatigue"],
        "reply": "Sleep tips:\n  - Adults need 7-9 hours per night\n  - Avoid screens 1 hour before bed\n  - Keep a consistent sleep schedule\n  - Try deep breathing to relax"
    },
    "stress": {
        "keywords": ["stress", "anxiety", "depressed", "sad", "worried", "overwhelmed"],
        "reply": "Mental Health support:\n  - You are not alone, help is available\n  - Talk to someone you trust\n  - Exercise and meditation really help\n  - iCall helpline (India): 9152987821"
    },
    "diet": {
        "keywords": ["diet", "nutrition", "healthy food", "weight loss", "calories"],
        "reply": "Diet tips:\n  - Eat more fruits and vegetables\n  - Drink 2-3 litres of water daily\n  - Limit sugar, salt, and fried food\n  - Include protein like eggs, lentils, and fish"
    },
    "covid": {
        "keywords": ["covid", "corona", "coronavirus", "omicron", "vaccine"],
        "reply": "COVID-19 info:\n  - Symptoms: fever, dry cough, loss of taste/smell\n  - Wear a mask and wash hands regularly\n  - Get vaccinated\n  - Isolate if you test positive"
    },
    "first_aid": {
        "keywords": ["first aid", "bleeding", "burn", "fracture", "wound", "cut"],
        "reply": "First Aid tips:\n  - Bleeding: press a clean cloth, elevate limb\n  - Burns: cool under running water for 10 mins\n  - Fracture: keep still, don't move the person\n  - Call 112 for serious emergencies"
    },
    "thanks": {
        "keywords": ["thanks", "thank you", "helpful", "great"],
        "reply": "You're welcome! Stay healthy!"
    },
    "bye": {
        "keywords": ["bye", "goodbye", "exit", "quit"],
        "reply": "Goodbye! Take care of yourself!"
    }
}

# ---------- SYMPTOM CHECKER ----------
SYMPTOM_COMBOS = [
    (["fever", "cough", "fatigue"],       "Could be COVID-19 or flu. Please see a doctor."),
    (["headache", "fever", "stiff neck"], "WARNING: Could be meningitis. Go to hospital immediately!"),
    (["chest pain", "breathless"],        "WARNING: Possible heart emergency. Call 112 now!"),
    (["nausea", "vomiting", "stomach"],   "Could be food poisoning. Rest and drink fluids."),
    (["fatigue", "weight loss"],          "Please visit a doctor for a proper checkup."),
]

# ---------- CHAT HISTORY ----------
history = []

def log(role, message):
    history.append({"time": datetime.now().strftime("%H:%M:%S"), "role": role, "message": message})

def show_history():
    if not history:
        print("  No history yet.\n")
        return
    for h in history:
        label = "You" if h["role"] == "user" else "MediBot"
        print(f"  [{h['time']}] {label}: {h['message']}")
    print()

def save_history():
    os.makedirs("data", exist_ok=True)
    with open("data/history.json", "w") as f:
        json.dump(history, f, indent=2)
    print("  Saved to data/history.json\n")

# ---------- FIND BEST TOPIC ----------
# Goes through every topic, counts how many keywords
# match the user's message, returns the best one.

def get_reply(message):
    message = message.lower()
    best_topic = None
    best_score = 0

    for topic in TOPICS:
        score = 0
        for keyword in TOPICS[topic]["keywords"]:
            if keyword in message:
                score += 1
        if score > best_score:
            best_score = score
            best_topic = topic

    if best_score > 0:
        return TOPICS[best_topic]["reply"]
    return None

# ---------- SYMPTOM CHECKER ----------
def symptom_checker():
    print("  Enter symptoms separated by commas (e.g. fever, cough, fatigue):")
    raw = input("  > ").lower().strip()
    symptoms = [s.strip() for s in raw.split(",")]

    best_advice = None
    best_count = 0

    for combo, advice in SYMPTOM_COMBOS:
        count = sum(1 for s in combo if s in symptoms)
        if count > best_count:
            best_count = count
            best_advice = advice

    if best_advice and best_count >= 2:
        print(f"\n  Result: {best_advice}\n")
    else:
        print("  No strong match. Please describe more symptoms or see a doctor.\n")

# ---------- MAIN CHAT LOOP ----------
def main():
    print("=" * 45)
    print("    MediBot - AI Medical FAQ Chatbot")
    print("    CSA2001 | Fundamentals of AI & ML")
    print("=" * 45)
    print("  Commands: help | symptoms | history | save | exit\n")

    while True:
        user = input("  You: ").strip()
        if not user:
            continue

        if user.lower() == "exit":
            print("  MediBot: Goodbye! Stay healthy!\n")
            break

        elif user.lower() == "help":
            print("\n  Topics: fever, cough, headache, stomach, diabetes,")
            print("  bp, sleep, stress, diet, covid, first aid")
            print("  Commands: symptoms, history, save, exit\n")

        elif user.lower() == "symptoms":
            symptom_checker()

        elif user.lower() == "history":
            show_history()

        elif user.lower() == "save":
            save_history()

        else:
            log("user", user)
            reply = get_reply(user)
            if reply:
                print(f"\n  MediBot: {reply}\n")
                log("bot", reply)
            else:
                print("  MediBot: I didn't understand that. Type 'help' to see topics.\n")

if __name__ == "__main__":
    main()
