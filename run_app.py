import os
import sys
import webbrowser
import threading
import time
from django.core.management import execute_from_command_line

try:
    import certifi
except ImportError:
    certifi = None


def configure_tls_certificates():
    if not certifi:
        return

    cert_path = certifi.where()
    os.environ.setdefault("SSL_CERT_FILE", cert_path)
    os.environ.setdefault("REQUESTS_CA_BUNDLE", cert_path)


def open_browser():
    time.sleep(2)
    webbrowser.open("http://127.0.0.1:8000")


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deliciousKitchen.settings")
    configure_tls_certificates()

    threading.Thread(target=open_browser, daemon=True).start()

    execute_from_command_line([
        "manage.py",
        "runserver",
        "127.0.0.1:8000",
        "--noreload"
    ])
