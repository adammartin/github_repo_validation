import os

API_TOKEN = 'INSERT_REAL_TOKEN_HERE'
SOURCE_ROOT_URL = 'https://api.github.com'
SOURCE_HEADER = {'Accept': 'application/vnd.github.mercy-preview+json'}
REPO_PROPERTIES = ['full_name', 'collaborators_url', 'topics', 'url']
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
