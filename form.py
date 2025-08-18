from app import createApp, db
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

app = createApp()
CORS(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug = True)
