"""Main wrapper"""
from website import create_app

notes_app = create_app()

if __name__ == "__main__":
    notes_app.run(port=5020, debug=True)
