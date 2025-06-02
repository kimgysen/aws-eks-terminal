import yaml
import os

def load_config():
    # Determine the project root (2 levels up from this file)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, "..", ".."))

    config_path = os.path.join(project_root, "config.yaml")
    local_config_path = os.path.join(project_root, "config.local.yaml")

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    if os.path.exists(local_config_path):
        with open(local_config_path, "r") as f:
            local_config = yaml.safe_load(f)
        if local_config is not None:
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
