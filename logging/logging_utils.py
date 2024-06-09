import logging
import sys


class Colors:
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    END = "\033[0m"
    BOLD = "\033[1m"
    ITALICS = "\033[3m"
    CRITICAL = "\033[1;41m"


class ColoredFormatter(logging.Formatter):
    def __init__(self, fmt, date_fmt):
        super().__init__()
        self.fmt = fmt
        self.date_fmt = date_fmt
        pattern = "%(levelname)s"
        _fmt = self.fmt.split(pattern)
        self.formats = {
            level: f"{Colors.ITALICS}{_fmt[0]}{Colors.BOLD}{color}{pattern}{Colors.END}{_fmt[1]}"
            for level, color in [
                (logging.DEBUG, Colors.BLUE),
                (logging.INFO, Colors.GREEN),
                (logging.WARNING, Colors.WARNING),
                (logging.ERROR, Colors.FAIL),
                (logging.CRITICAL, Colors.CRITICAL),
            ]
        }

    def format(self, record):
        log_fmt = self.formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt=self.date_fmt)
        return formatter.format(record)


def get_custom_logger(**kwargs):
    logger = logging.getLogger()
    stream_level = kwargs.get("level", "INFO")
    file_handler_level = kwargs.get("file_handler_level", "INFO")
    root_level = min([logging.getLevelName(k) for k in (stream_level, file_handler_level)])

    logger.setLevel(level=root_level)
    logger.handlers = []

    # Formatting
    fmt = kwargs.get(
        "fmt",
        "%(asctime)s - %(process)d - {%(filename)s:%(lineno)d} - "
        "%(funcName)s - %(levelname)s - %(message)s",
    )
    date_fmt = kwargs.get("datefmt", "%Y-%m-%d %H:%M:%S")
    formatter = logging.Formatter(fmt, date_fmt)

    # Stream Handler
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setLevel(level=stream_level)
    if kwargs.get("stream_fmt") == "color":
        stream_handler.setFormatter(ColoredFormatter(fmt, date_fmt))
    else:
        stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    filename = kwargs.get("filename")
    if filename:
        file_handler = logging.FileHandler(
            filename,
            mode=kwargs.get("mode", "a"),
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level=file_handler_level)
        logger.addHandler(file_handler)

    return logger
