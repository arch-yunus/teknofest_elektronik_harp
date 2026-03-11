import sys
import os
import webview
import threading

# Import the existing Flask app
from src.dashboard.app import app

def start_server():
    # Run the flask app on a specific port in a separate thread
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)

if __name__ == '__main__':
    print("[Aegis-AI] Başlatılıyor: Masaüstü Arayüzü...")
    
    # Start the Flask server in a background thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # Create the native desktop window pointing to the local Flask server
    window = webview.create_window(
        title='Aegis-AI | Taktik Elektronik Harp Kontrol Paneli',
        url='http://127.0.0.1:5000',
        width=1280,
        height=800,
        resizable=True,
        frameless=False, # Set to True if we want a completely custom title bar
        background_color='#050a14'
    )
    
    # Start the webview application loop
    webview.start()
