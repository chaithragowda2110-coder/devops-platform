from flask import Flask, render_template, jsonify
import platform, datetime, os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',
        host=platform.node(),
        time=datetime.datetime.now().strftime("%H:%M:%S"),
        env=os.environ.get("APP_ENV", "production")
    )

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/info')
def info():
    return jsonify({
        "app": "DevOps Deployment Platform",
        "version": "1.0",
        "cloud": "AWS EC2",
        "container": platform.node()
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)