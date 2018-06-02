import os

API_TOKEN = 'INSERT_REAL_TOKEN_HERE'
SOURCE_ROOT_URL = 'https://api.github.com'
SOURCE_HEADER = {'Accept': 'application/vnd.github.mercy-preview+json'}
REPO_PROPERTIES = ['full_name', 'topics', 'url']
ORGANIZATIONS = ['digital-solutions',
                 'immersion-active',
                 'marketing',
                 'hisc',
                 'it-services',
                 'it-support',
                 'it',
                 'finance']
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
