from main import greet

def test_greet_default():
    assert greet() == "Hello from GitHub Actions!"

def test_greet_custom():
    assert greet("Pragadeeshwar") == "Hello from Pragadeeshwar!"
