import uvicorn
import sys

from app import app
from configparser import ConfigParser

config = ConfigParser()

PORT = config.get("defalut", "PORT") | 5000

reload = False
if len(sys.argv) >= 2:
    if sys.argv[1] == "-R":
        reload = True

if __name__ == "__main__":
    uvicorn.run("main:app", port = PORT, reload = reload)



