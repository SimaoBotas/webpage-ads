from src import main 

def test_hello_world(capsys):
    
    main  
    captured = capsys.readouterr()
    assert "Hello world" in captured.out