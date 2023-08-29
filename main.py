"""Main wrapper"""
import os
from website import create_app

notes_app = create_app(debug=True)

if __name__=="__main__":
    notes_app.run(
        port=os.environ.get("PORT"),
        load_dotenv=True,
        )