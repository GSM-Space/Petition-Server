import uvicorn
import sys

from app.app import app
from configparser import ConfigParser

config = ConfigParser()

PORT = config.get("defalut", "PORT") | 5000

reload = False
if len(sys.argv) >= 2:
    if "-R" in sys.argv[1]:
        reload = True
    if "PORT=" in sys.argv[-1]:
        PORT = sys.argv[-1][5:]

if __name__ == "__main__":
    uvicorn.run("main:server", port = PORT, reload = reload)



