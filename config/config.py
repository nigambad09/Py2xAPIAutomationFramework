import yaml


class Config:
    @staticmethod
    def load():
        with open("config/config.yaml") as f:
            return yaml.safe_load(f)

    @staticmethod
    def url():
        return Config.load()["app"]["url"]

    @staticmethod
    def browser():
        return Config.load()["browser"]["name"]
