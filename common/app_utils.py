import os

import yaml

# from common.redis import redis


class AppUtils:
    """
    Stores some app data like config
    """

    def __init__(self):
        self.config = None

    def init_app(self, env : str = "local") -> None:
        """
        initiates AppUtils
        :return: None
        """
        config_name = os.getenv("POPULATOR_CONFIG") or "local"
        with open("config/default.yaml", "r") as yaml_file:
            self.config = yaml.load(yaml_file, yaml.FullLoader)
        with open("config/%s.yaml" % env, "r") as yaml_file:
            self.config = {**self.config, **yaml.load(yaml_file, yaml.FullLoader)}

        self.config["ENV"] = config_name
        # # Redis init
        # redis.init_app(self)


app_utils = AppUtils()