import yaml
import os

def load_config():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    if os.path.exists("config.local.yaml"):
        with open("config.local.yaml", "r") as f:
            local_config = yaml.safe_load(f)
        if not local_config is None:
            merge_dicts(config, local_config)

    return config

def merge_dicts(a, b):
    """
    Recursively merge dictionary b into dictionary a
    """
    for key, value in b.items():
        if isinstance(value, dict) and key in a and isinstance(a[key], dict):
            merge_dicts(a[key], value)
        else:
            a[key] = value