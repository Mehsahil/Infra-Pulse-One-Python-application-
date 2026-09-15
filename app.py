from flask import Flask, render_template, jsonify
import platform
import shutil
import socket
import time
from datetime import datetime

try:
    import psutil
except ImportError:
    psutil = None

app = Flask(__name__)
START_TIME = time.time()

def system_info():
    memory = psutil.virtual_memory() if psutil else None
    disk = shutil.disk_usage("/")
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.release(),
        "python": platform.python_version(),
        "cpu_percent": psutil.cpu_percent(interval=0.2) if psutil else 0,
        "memory_percent": memory.percent if memory else 0,
        "disk_percent": round((disk.used / disk.total) * 100, 1),
        "uptime_seconds": int(time.time() - START_TIME),
        "timestamp": datetime.now().strftime("%d %b %Y, %H:%M:%S"),
    }

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/api/metrics")
def metrics():
    return jsonify(system_info())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
