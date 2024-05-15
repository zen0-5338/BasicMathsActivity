from datetime import datetime
import logging
from os import path


LOG_FORMAT = "[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s"
# SHORT_LOG_FORMAT = "[%(asctime)s] %(levelname)-8s: %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
# SHORT_DATE_FORMAT = "%Y-%m-%d_%H-%M-%S"

logging.basicConfig(
    level=logging.DEBUG,
    filename=path.join(
        "./logs",
        f'{datetime.strftime(datetime.now(),"_".join([DATE_FORMAT.split(" ")[0],DATE_FORMAT.split(" ")[1].replace(":","-")]))}.log',
    ),
    filemode="a",
    format=LOG_FORMAT,
    datefmt=DATE_FORMAT,
)
logger = logging.getLogger("basic-maths-activity")

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT))
logger.addHandler(console)

