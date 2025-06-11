import subprocess

def fetch_eks_namespaces():
    print("Fetching namespaces...")
    try:
        result = subprocess.run(f"kubectl get namespaces -o jsonpath={{.items[*].metadata.name}}", capture_output=True, text=True, check=True)
        return result.stdout.strip().split()
    except subprocess.CalledProcessError:
        print("--> :'( Fetching namespaces failed.")
        exit(1)

def fetch_eks_pods(namespace):
    print(f"Fetching pods in namespace: {namespace}")
    try:
        result = subprocess.run(f"kubectl get pods -n {namespace} -o jsonpath={{.items[*].metadata.name}}",
                                             capture_output=True, text=True, check=True)
        return result.stdout.strip().split()
    except subprocess.CalledProcessError:
        print("--> :'( Fetching pods failed.")
        exit(1)

def pod_debug(namespace, pod, port):
    print(f"Starting debug session for pod: {pod}")

    user_input = input(f"Enter local port to use (press Enter to use default: {port}): ")
    local_port = user_input.strip() or port  # Use entered port or default if blank

    try:
        subprocess.run(
            f"kubectl port-forward {pod} {local_port}:{local_port} -n {namespace}",
            shell=True,
            check=True  # Ensures CalledProcessError is raised on failure
        )
    except subprocess.CalledProcessError:
        print("--> :'( Opening debug port failed.")
        exit(1)
    except KeyboardInterrupt:
        print("\n--> Port forwarding interrupted by user.")

    input("\nPress Enter to return to the menu...")

def pod_log(namespace, pod, tail):
    print(f"Opening log for pod: {pod}")
    try:
        subprocess.run(f"kubectl logs -f --tail={tail} {pod} -n {namespace}", shell=True)
    except subprocess.CalledProcessError:
        print("--> :'( Opening pod log failed.")
        exit(1)
    except KeyboardInterrupt:
        print("\n--> Log streaming interrupted by user.")
    input("\nPress Enter to return to the menu...")

def pod_login(namespace, pod):
    print(f"Login pod: {pod}")
    try:
        subprocess.run(f"kubectl exec -it {pod} -n {namespace} -- /bin/bash", shell=True)
    except subprocess.CalledProcessError:
        print("--> :'( Login pod failed.")
        exit(1)
    except KeyboardInterrupt:
        print("\n--> Pod session ended.")
    input("\nPress Enter to return to the menu...")

def fetch_resources(namespace, resource_type):
    print(f"{resource_type}s for namespace: {namespace}")

    if resource_type != "ingress":
        resource_type += "s"

    try:
        result = subprocess.run(f"kubectl get {resource_type} -n {namespace} -o name",
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True)
        # Each line is a resource like "pod/foo"
        return result.stdout.strip().splitlines()
    except subprocess.CalledProcessError:
        print("--> :'( Fetching resources failed.")
        exit(1)

def open_resource(namespace, resource):
        print(f"open {resource}s for namespace: {namespace}")
        try:
            subprocess.run(f'cmd /c "kubectl get {resource} -n {namespace} -o yaml & pause"', check=True, shell=True)
        except subprocess.CalledProcessError:
            print("--> :'( Fetching resources failed.")
            exit(1)