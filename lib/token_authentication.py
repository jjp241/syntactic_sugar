import os
import json
from pathlib import Path


TOKEN_NAME = 'user_token.json'


def get_token_path():
    return Path('/media') / os.getlogin() / 'GOLDTOKEN'


def is_token_file_present():
    """ Check devices and if token is present return True """
    token_path = get_token_path()

    try:
        present_files = list(os.listdir(token_path))

        return len(present_files) > 0
    except Exception:
        return False


def get_goldman_token_value():
    token_path = get_token_path()

    present_files = None
    try:
        present_files = list(os.listdir(token_path))
    except FileNotFoundError:
        raise ValueError("No token found!")

    if TOKEN_NAME in present_files:
        with open(token_path / TOKEN_NAME) as f:
            token_data = json.load(f)
            if 'token' not in token_data:
                raise ValueError("No token code!")
            
            return token_data['token']
    
    raise ValueError("No token found!")
