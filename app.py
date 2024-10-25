from config import app
from config import tasks

app.register_blueprint(tasks)


app.run(host='0.0.0.0', port=5000, debug=True)
