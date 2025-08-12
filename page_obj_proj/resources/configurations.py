import configparser
import os

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
resources_dir = os.path.join(proj_dir, "resources")
config_path = os.path.join(resources_dir, "properties.ini")

def get_url(url):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config['URL'][url]

def get_selgridurl(selurl):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config['SELGRID_URL'][selurl]

