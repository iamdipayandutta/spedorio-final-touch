import sys
import os

# Add your project directory to the path
# IMPORTANT: Change this to your PythonAnywhere username
username = 'yourusername'  # Replace with your actual PythonAnywhere username
path = f'/home/{username}/spedorio-website/backend'

if path not in sys.path:
    sys.path.append(path)

# Set the working directory
os.chdir(path)

# Import the Flask app
from app import app as application

# Add any environment variables
os.environ['SECRET_KEY'] = 'your-secret-key-change-this'
os.environ['DATABASE_URL'] = 'sqlite:///blog.db'

# This file is used by PythonAnywhere to serve your application
# Instructions for use:
# 1. Upload this file to PythonAnywhere
# 2. Configure your web app to use this file as the WSGI configuration file
# 3. Replace 'yourusername' with your actual PythonAnywhere username 