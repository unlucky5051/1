import logging
import os

path = r"D:\PycharmProjects\pythonSiteToOffice\log.txt"
absolute_path_log = os.path.abspath(path)
logging.basicConfig(level=logging.INFO,filename=absolute_path_log,filemode='a', format="%(name)s: %(asctime)s %(levelname)s %(message)s")

#
# logging.basicConfig(level=logging.INFO, filename=path,
#                     format="%(asctime)s %(levelname)s %(message)s")


