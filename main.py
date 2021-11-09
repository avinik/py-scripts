import argparse

from common import app_utils

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e", "--env", required=False, help="Application environment", default="local"
    )

    args = vars(parser.parse_args())
    env = args["env"]
    app_utils.init_app(env)
    