import subprocess

def test_output():
    # Führe das Python-Programm aus
    result = subprocess.run(["python", "hello.py"], capture_output=True, text=True)
    
    # Überprüfe, ob die Ausgabe "Hello, World!" entspricht
    assert result.stdout.strip() == "Hello, World!", "Die Ausgabe ist falsch!"
