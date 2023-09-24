import os
from pathlib import Path
import logging
import sys
logging_format='[%(asctime)s - %(name)s - %(levelname)s - %(message)s]'
logsfile='logs'
logs_path=os.path.join(logsfile,'logs.log')
os.makedirs(logsfile,exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_format,
    handlers=[logging.FileHandler(logs_path),
              logging.StreamHandler(sys.stdout)]
)
logger=logging.getLogger("Risk Analysis")