import logging
import datetime
from colorama import Fore
import json
import yaml


class CustomLog:
    COLOR_GREEN = Fore.GREEN
    COLOR_BLUE = Fore.BLUE
    COLOR_AMBER = Fore.LIGHTYELLOW_EX
    COLOR_RED = Fore.RED
    COLOR_WHITE = Fore.LIGHTWHITE_EX

    def __init__(self, name: str):
        self.handler = logging.StreamHandler()
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

    def box_log(self, message: str, color=COLOR_GREEN):
        """
        Method for box style log
        :param message: message that should be logged
        :param color: selected color
        """
        box_width = len(message) + 2
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        box_formatter = logging.Formatter(f'{color} | %(message)s |')
        self.handler.setLevel(logging.INFO)
        self.handler.setFormatter(box_formatter)
        self.logger.addHandler(self.handler)
        self.logger.info(color + "+" + "-" * box_width + "+")
        self.logger.info(color + "|" + " " * ((box_width - len(message)) // 2) + message + " " * (
                (box_width - len(message) + 1) // 2) + "|")
        self.logger.info(color + "|" + " " * ((box_width - len(timestamp)) // 2) + timestamp + " " * (
                (box_width - len(timestamp) + 1) // 2) + "|")
        self.logger.info(color + "+" + "-" * box_width + "+")

    def title_log(self, title: str, message: str, color=COLOR_GREEN):
        """
        Method for title style log
        :param title: log's title
        :param message: message that should be logged
        :param color: selected color
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        title = f'====== {title}  ======'
        title_timestamp = f'=== {timestamp}  ==='
        message_line = ' ' * 8 + message + ' ' * 8
        max_width = max(len(title), len(title_timestamp), len(message_line))
        title = title.center(max_width)
        title_timestamp = title_timestamp.center(max_width)
        message_line = message_line.center(max_width)
        box_formatter = logging.Formatter(f'{color} | %(message)s |')
        self.handler.setLevel(logging.INFO)
        self.handler.setFormatter(box_formatter)
        self.logger.addHandler(self.handler)
        self.logger.info(color + title)
        self.logger.info(color + title_timestamp)
        self.logger.info(color + message_line)

    def json_log(self, title, message: str, data: dict, color=COLOR_GREEN):
        """
        Method for JSON style log
        :param title: log's title
        :param message: message that should be logged
        :param data: data that should be presented in JSON format
        :param color: selected color
        """
        json_formatter = logging.Formatter(f'{color}  %(message)s ')
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.handler.setLevel(logging.INFO)
        self.handler.setFormatter(json_formatter)
        self.logger.addHandler(self.handler)
        log_entry = {
            title: {
                "timestamp": timestamp,
                "level": logging.getLevelName(self.handler.level),
                "message": message,
                "data": data
            }
        }
        log_string = json.dumps(log_entry, indent=4)
        self.logger.info(color + log_string)
        self.logger.removeHandler(self.handler)

    def yaml_log(self, title, message: str, data: dict, color=COLOR_GREEN):
        """
        Method for YAML style log
        :param title: log's title
        :param message: message that should be logged
        :param data: data that should be presented in YAML format
        :param color: selected color
        """
        yml_formatter = logging.Formatter(f'{color}  %(message)s ')
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.handler.setLevel(logging.INFO)
        self.handler.setFormatter(yml_formatter)
        self.logger.addHandler(self.handler)
        log_entry = {
            title: {
                "timestamp": timestamp,
                "level": logging.getLevelName(self.handler.level),
                "message": message,
                "data": data
            }
        }
        yaml_string = yaml.dump(log_entry, default_style="", default_flow_style=False, sort_keys=False)
        self.logger.info(color + yaml_string)
        self.logger.removeHandler(self.handler)
