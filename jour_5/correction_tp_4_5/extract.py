"""
module pour extraire des emails depuis une chaine de caracteres 
"""
import os
import re

def extract_emails(path: str) -> list[str]:
    """
        Extrait les email et retroune une list
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"le fichier {path} est introuvable!")
    emails = set()
    pattern = r"[a-zA-Z0-9.+]+@[a-zA-Z0-9.+]+\.[a-z]{2,}"
    with open(path,"r",encoding="utf-8") as f:
        for line in f:
            for match in re.findall(pattern, line):
                emails.add(match)
    return sorted(emails)
