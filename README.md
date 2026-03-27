# 🏥 MediBot — AI-Powered Medical FAQ Chatbot (CLI)

> A rule-based NLP chatbot that answers common health and medical queries through a fully interactive command-line interface.

**Course:** Fundamentals of AI and ML — CSA2001  
**Type:** BYOP (Bring Your Own Project) — Capstone Submission  
**Language:** Python 3 | No external API required

---

## 📌 What Does MediBot Do?

MediBot is a CLI-based intelligent chatbot that:

- Understands natural language health queries using **rule-based NLP**
- Provides information on **symptoms, medicines, first aid, and wellness**
- Uses **keyword extraction** and **fuzzy string matching** (`difflib`) to handle varied phrasing
- Maintains a **chat history** and allows saving it to a JSON file
- Runs entirely in the terminal — no GUI, no internet, no API key needed

---

## 🧠 AI/ML Concepts Applied

| Concept | How It's Used |
|---|---|
| Natural Language Processing (NLP) | Text preprocessing, tokenization, stopword removal |
| Pattern Matching | Intent detection via keyword rules |
| Fuzzy Matching | `difflib.get_close_matches` for typo-tolerant matching |
| Knowledge Base | Structured intent–response mapping |
| Information Retrieval | Keyword-based query-to-answer lookup |

---

## 🗂️ Project Structure

```
MediBot/
├── chatbot.py       # Main application (all logic in one file)
├── README.md        # This file
└── chat_history_*.json   # Auto-generated when you save history
```

---

## ⚙️ Requirements

- **Python 3.6 or higher**
- No third-party libraries needed — uses only Python standard library:
  - `re` — Regular expressions for text cleaning
  - `json` — Saving chat history
  - `os` — Screen clearing
  - `datetime` — Timestamping logs
  - `difflib` — Fuzzy keyword matching

---

## 🚀 Setup & Running

### Step 1: Clone the Repository

```bash
git clone https://github.com/{your-username}/MediBot.git
cd MediBot
```

### Step 2: Verify Python Installation

```bash
python3 --version
# Should output Python 3.6 or higher
```

### Step 3: Run the Chatbot

```bash
python3 chatbot.py
```

That's it — no `pip install` needed!

---

## 💬 How to Use

Once started, you'll see the MediBot banner and a prompt:

```
  You: _
```

### Example Queries

```
You: I have a fever
You: Tell me about diabetes
You: What is paracetamol used for?
You: First aid for burns
You: I feel stressed
You: what vaccines should I take
```

### Built-in Commands

| Command | Description |
|---|---|
| `help` | Show all commands and topics |
| `topics` | List all health topics MediBot covers |
| `history` | View conversation history for this session |
| `save` | Save chat history to a JSON file |
| `clear` | Clear the terminal screen |
| `exit` / `quit` | Exit MediBot |

---

## 📋 Topics Covered

| Category | Topics |
|---|---|
| Symptoms | Fever, Cold, Headache, Cough |
| Chronic Diseases | Diabetes, Hypertension |
| Medicines | Paracetamol, Ibuprofen |
| First Aid | Burns, Cuts & Wounds |
| Wellness | Sleep, Diet, Exercise, Stress |
| Preventive | Vaccination |
| Emergency | Emergency numbers & CPR guidance |

---

## 🔍 How the NLP Works

```
User Input
    │
    ▼
Preprocessing (lowercase, remove punctuation)
    │
    ▼
Stopword Removal (extract meaningful keywords)
    │
    ▼
Pattern Matching (check against knowledge base)
    │
    ├── Match found? → Return response
    │
    └── No match? → Fuzzy matching with difflib
                        │
                        ├── Close match? → Return response
                        └── No match?  → Show suggestions + fallback
```

---

## ⚠️ Disclaimer

MediBot is built for **educational purposes only** as part of an AI/ML course project. It does **not** provide real medical advice. Always consult a qualified healthcare professional for medical decisions.

---

## 👤 Author

**Student Name:** [Your Name]  
**Reg No:** [Your Registration Number]  
**Course:** Fundamentals of AI and ML — CSA2001
