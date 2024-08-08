# modules/__init__.py
import logging
# You can import modules from the package
from .config_reader import *
from .date_util import *
from .file_reader import *
from .file_util import *
from .transfer_util import *

# You can define any initialization code here if needed
# For example:
logging.info("Initializing the 'modules' package...")
