import logging
import math

LOG_FORMAT = "%(levelname)s %(asctime)s %(message)s"
logging.basicConfig(filename="/Users/margarita/Documents/Python-exapmles/lumberjeck.log", level=logging.DEBUG,
                    format=LOG_FORMAT, filemode="w")
logger = logging.getLogger()
logger.info("Our second massage")
print(logger.level)


def quadratic(a, b, c):
    if c < 0:
        logger.info("quadratic({0}, {1}, {2})".format(a, b, c))
        logger.debug("#compute the discrimant")
        disc = b ** 2 - 4 * a * c
        logger.debug("compute roots")
        root1 = (-b + math.sqrt(disc) / (2 * a))
        root2 = (-b - math.sqrt(disc) / (2 * a))
        logger.debug("# return the roots")
        return root1, root2
    else:
        logger.error("invaldi input, c must be negative")
        print("c needs to bee negative")


roots = quadratic(1, 0, 4)
print(roots)
