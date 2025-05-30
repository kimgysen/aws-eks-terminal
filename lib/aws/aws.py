import os
import subprocess
import json

def run_sso_login(profile):
    print(f"Logging in to AWS SSO with profile: {profile}")
    try:
        subprocess.run(["aws", "sso", "login", "--profile", profile], check=True, env={**os.environ})
    except subprocess.CalledProcessError:
        print("--> :'( SSO login failed.")
        exit(1)

def fetch_clusters(profile, region):
    try:
        result = subprocess.run(
                    ["aws", "eks", "list-clusters", "--profile", profile, "--region", region], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        data = json.loads(result.stdout)
        return data.get("clusters", [])
    except subprocess.CalledProcessError:
        print("--> :'( Fetching clusters failed.")
        exit(1)

def update_kubeconfig(cluster_name, region, profile):
    print(f"--> Updating kubeconfig for EKS cluster: {cluster_name}")
    try:
        subprocess.run([
            "aws", "eks", "update-kubeconfig",
            "--name", cluster_name,
            "--region", region,
            "--profile", profile
        ], check=True)
    except subprocess.CalledProcessError:
        print("--> :'( Updating kubeconfig failed.")
        exit(1)