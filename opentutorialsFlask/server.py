from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'random : <strong>' + str(random.randint(0, 100)) + '</strong>'

if __name__ == "__main__":
    app.run(port=3000, debug=True)  # 개발 중에는 debug=True로 디버깅 모드로 해도 괜찮다. 실제 서비스에서는 하면 안된다.