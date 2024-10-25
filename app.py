from config import app
from config import task

app.register_blueprint(task)


app.run(host='0.0.0.0', port=5000, debug=True)
