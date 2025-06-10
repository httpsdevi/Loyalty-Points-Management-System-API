# run.py
import webbrowser
import subprocess
import time

# Open the docs URL after a short delay
def launch_browser():
    time.sleep(1)
    webbrowser.open("http://127.0.0.1:8000/docs")

if __name__ == "__main__":
    # Start the browser in a new thread
    import threading
    threading.Thread(target=launch_browser).start()

    # Start the FastAPI server
    subprocess.run(["uvicorn", "main:app", "--reload"])
