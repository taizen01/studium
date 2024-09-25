users = [
    {"name": "Alice", "email": "alice@example.com", "phone": "12345"},
    {"name": "Bob", "email": "", "phone": "67890"},      # Ungültiger Eintrag
    {"name": "Charlie", "phone": None}                  # Ungültiger Eintrag
]

# Durchlaufe die Liste der Benutzer, um ihre Informationen zu überprüfen
for user in users:
    # Iteriere über alle Schlüssel-Wert-Paare im aktuellen Benutzer-Dictionary
    for key, value in user.items():
        # Überprüfe, ob der Wert None oder ein leerer String ist
        if value is None or value == "":
            # Wenn der Wert ungültig ist, gib eine Nachricht aus
            print("User hat mind. einen ungültigen Eintrag")

