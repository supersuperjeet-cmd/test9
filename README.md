# Jeet 💙 - AI Boyfriend Telegram Bot

## Overview
Jeet 💙 is a smart, caring AI boyfriend bot running 24/7 on Telegram with a secret web interface for Aradhya. Features smart memory retention with time-aware context, meaningful conversations, romantic games, and a beautiful admin dashboard for complete control.

## Project Structure
- `main.py`: Flask server + Telegram bot + AI logic
- `templates/`: Login, chat interface, admin dashboard
- `static/`: User music library and assets
- `requirements.txt`: All dependencies
- `Procfile`: Render deployment configuration
- `EASY_DEPLOY.md`: Step-by-step hosting guide
- `CODESPACE_TEST.md`: Instructions for testing on GitHub Codespaces

## Key Features
✨ **Smart Memory**: Chat history automatically loads and influences responses
⏰ **Time-Aware**: Knows if it's morning/afternoon/evening and adapts
💬 **Meaningful Chats**: Uses recent history to understand preferences
🎮 **7 AI Games**: Tic Tac Toe, Guess Number, Love Quiz, RPS, Kiss/Slap, Word Scramble, Riddles
🎵 **Music System**: Click sound + play/mute + admin upload/delete
📔 **Diary**: Save unlimited notes, user delete own, admin control all
🛠️ **Mobile Menu**: 3-line hamburger menu for easy navigation

## Setup Status ✅
- ✅ Python 3.11 installed
- ✅ SQLite/PostgreSQL database support (Auto-fallback)
- ✅ All dependencies listed in requirements.txt
- ✅ Flask server running on port 5000
- ✅ Deployment configured for Render/Codespaces

## Hosting / Deployment
Refer to `EASY_DEPLOY.md` for Render hosting instructions and `CODESPACE_TEST.md` for GitHub Codespaces testing.

## Environment Variables Needed
- `OPENAI_API_KEY`: Get from OpenAI
- `TG_TOKEN`: Get from @BotFather
- `OWNER_ID`: Your Telegram user ID
- `GF_NAME`: Aradhya
- `BOT_NAME`: Jeet
- `WEB_PASSWORD`: love u

Additional (Render / Web) environment variables
- `GROQ_API_KEY`: Groq AI API key (get from https://console.groq.com) — one of the primary AI providers used by the web app.
- `DATABASE_URL`: PostgreSQL connection string for persistent storage (Neon, Render Postgres, etc.). Example: `postgresql://user:pass@host:5432/dbname`. If omitted, the app falls back to local `db.json` (TinyDB).

Note: `psycopg2-binary` is included in `requirements.txt` to enable PostgreSQL connectivity (Neon/Postgres).

DB connectivity test
--------------------
There's a helper script `db_check.py` to verify `DATABASE_URL` is configured and that the app can perform basic read/write operations.

Run:
```bash
export DATABASE_URL='postgresql://user:pass@host:5432/dbname'
python db_check.py
```

If the script reports success, your Postgres/Neon connection is working and the app can transfer data.
