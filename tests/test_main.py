import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import main

def test_add():
    assert main.add(1, 1) == 2
    assert main.add(2, 3) == 5