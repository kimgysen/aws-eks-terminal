from lib.util.config_loader import load_config
from lib.aws.aws import *
from lib.aws.eks import *

CONFIG = load_config()
REGION = CONFIG["aws"]["region"]

def get_profiles(ctx):
    return CONFIG["aws"]["profiles"]

def handle_select_profile(ctx, profile):
    run_sso_login(profile)
    ctx["profile"] = profile
    return "select_cluster", "profile"
###
def get_clusters(ctx):
    return fetch_clusters(ctx["profile"], REGION)

def handle_select_cluster(ctx, cluster_name):
    update_kubeconfig(cluster_name, REGION, ctx["profile"])
    ctx["cluster"] = cluster_name
    return "select_namespace", "cluster"

###
def get_namespaces(ctx):
    return fetch_eks_namespaces()

def handle_select_namespace(ctx, namespace):
    ctx["namespace"] = namespace
    return "select_namespace_choice", "namespace"

###
def get_namespace_choices(ctx):
    return ["pods", "k8_resources"]

def handle_select_namespace_choice(ctx, ns_choice):
    match ns_choice:
        case "pods":
            return "select_pod", "namespace_choice"
        case "k8_resources":
            return "select_resource_type", "namespace_choice"

###
def get_pods(ctx):
    return fetch_eks_pods(ctx["namespace"])

def handle_select_pod(ctx, pod):
    ctx["pod"] = pod
    return "select_pod_choice", "pod"

###
def get_pod_choices(ctx):
    return ["debug", "log", "login"]

def handle_select_pod_choice(ctx, pod_choice):
    match pod_choice:
        case "debug":
            pod_debug(ctx["namespace"], ctx["pod"], "8000")
            return
        case "log":
            pod_log(ctx["namespace"], ctx["pod"], "5000")
            return
        case "login":
            pod_login(ctx["namespace"], ctx["pod"])
            return

###
def get_resource_types(ctx):
    return ["deployment", "configmap", "secret", "ingress"]

def handle_select_resource_type(ctx, resource_type):
    ctx["resource_type"] = resource_type
    return "select_resource", "resource_type"

###
def get_resources(ctx):
    return fetch_resources(ctx["namespace"], ctx["resource_type"])

def handle_select_resource(ctx, resource):
    open_resource(ctx["namespace"], resource)
