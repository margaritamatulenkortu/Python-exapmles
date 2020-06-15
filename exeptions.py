import logging
import time

logging.basicConfig(filename='/Users/margarita/Documents/Python-exapmles/exeptions.log', level=logging.DEBUG)
logger = logging.getLogger()


def read_file_timed(path):
    """REturns the conntents of the file at path"""
    start_time = time.time()
    try:
        f = open(path, mode='rb')
        datas = f.read()
        return datas
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("time required for {file} = {time}".format(file=path, time=dt))


datas = read_file_timed("/Users/margarita/Downloads/movie.mkv")
