#!/usr/bin/env python
import os
import sys
import subprocess

def setup_and_run():
    print("🚀 Setting up AI Agent...")
    
    # Install dependencies
    print("📦 Installing dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    
    # Run migrations
    print("🔄 Running migrations...")
    subprocess.run([sys.executable, "manage.py", "makemigrations"], check=True)
    subprocess.run([sys.executable, "manage.py", "migrate"], check=True)
    
    # Start server
    print("🌐 Starting Django server...")
    print("✅ AI Agent will be available at: http://127.0.0.1:8000")
    subprocess.run([sys.executable, "manage.py", "runserver"])

if __name__ == "__main__":
    setup_and_run()