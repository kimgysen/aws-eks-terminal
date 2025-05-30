import os
from lib.util.config_loader import load_config
from lib.menu.interactive_menu import MenuSystem
from lib.menu.menu_config import MENU_CONFIG


CONFIG = load_config()
REGION = CONFIG["aws"]["region"]
PROFILES = CONFIG["aws"]["profiles"]

os.environ["AWS_CA_BUNDLE"] = CONFIG["aws"]["ca-bundle"]

def main():
    system = MenuSystem(MENU_CONFIG, "select_profile")
    system.run()

if __name__ == "__main__":
    main()