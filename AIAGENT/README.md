# AI Agent - Django Chat Application

A simple AI-powered chat application built with Django and Google's Gemini AI.

## Features
- Clean, responsive UI with Tailwind CSS
- Real-time chat with Google Gemini AI
- Message history storage
- Simple setup and deployment

## Quick Start

1. **Install and Run:**
   ```bash
   python run.py
   ```

2. **Manual Setup (alternative):**
   ```bash
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

3. **Access the application:**
   Open http://127.0.0.1:8000 in your browser

## Configuration
- Update `.env` file with your Google API key
- Modify `GOOGLE_API_KEY` in the `.env` file

## Tech Stack
- **Backend:** Django 4.2.7
- **Frontend:** HTML, Tailwind CSS, JavaScript
- **AI:** Google Generative AI (Gemini)
- **Database:** SQLite (default)