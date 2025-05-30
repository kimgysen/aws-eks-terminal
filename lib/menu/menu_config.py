from lib.menu.handlers import *

MENU_CONFIG = {
    "select_profile": {
        "title": "Select profile",
        "options": get_profiles,
        "handler": handle_select_profile
    },
    "select_cluster": {
        "title": "Select cluster",
        "options": get_clusters,
        "handler": handle_select_cluster
    },
    "select_namespace": {
        "title": "Select namespace",
        "options": get_namespaces,
        "handler": handle_select_namespace
    },
    "select_namespace_choice": {
        "title": "Select namespace choice",
        "options": get_namespace_choices,
        "handler": handle_select_namespace_choice
    },
    "select_pod": {
        "title": "Select pod",
        "options": get_pods,
        "handler": handle_select_pod
    },
    "select_pod_choice": {
        "title": "Select pod choice",
        "options": get_pod_choices,
        "handler": handle_select_pod_choice
    },
    "select_resource_type": {
        "title": "Select resource type",
        "options": get_resource_types,
        "handler": handle_select_resource_type
    },
    "select_resource": {
        "title": "Select a resource",
        "options": get_resources,
        "handler": handle_select_resource
    }
}
