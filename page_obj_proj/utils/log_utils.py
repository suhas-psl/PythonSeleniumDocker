import logging
import os


proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
outputs_dir = os.path.join(proj_dir, "outputs")
logfile_path = os.path.join(outputs_dir, "project.log")

def setup_logger(name):

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')

    fh = logging.FileHandler(logfile_path)
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    return logger