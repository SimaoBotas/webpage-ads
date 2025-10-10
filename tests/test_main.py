# tests/test_main.py
import sys
import os

# Adiciona a raiz do projeto ao caminho de importação
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import main  # agora deve funcionar

def test_hello_world(capsys):
    main  # executa o print do main.py
    captured = capsys.readouterr()  # captura a saída do print
    assert "Hello world" in captured.out
