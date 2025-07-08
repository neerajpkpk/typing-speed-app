#!/usr/bin/env bash
# Render build script
echo "📦 Installing dependencies..."
pip install -r requirements.txt
echo "🔨 Running migrations..."
python manage.py migrate
echo "📦 Collecting static files..."
python manage.py collectstatic --no-input
