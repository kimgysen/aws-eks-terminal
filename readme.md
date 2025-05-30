# aws-eks-terminal

Access AWS EKS cluster info fast across different environments / profiles.
Simple interactive terminal app with selectable drill-down submenus using arrows. 
Written in Python, runs on Windows Powershell. 

## Features

- List / select profiles: auto SSO login
- List / select cluster: auto update-kubeconfig
- List / select namespaces 
- Pod utilities:
  - Pod logs
  - Log in container (interactive terminal)
  - Pod debug (can be made more dynamic)
- View k8 resources (read-only): 
  - Deployments
  - Configmaps
  - Secrets
  - Ingress

## Prerequisites

- AWS SSO / start page setup 
- AWS EKS cluster setup 
- Install python3, aws-cli, kubectl (kubernetes cli)
- Create profiles in aws .config with sso_session, sso_account_id, sso_role_name
- Save certificate (pem or crt) on hard drive

## Usage

The config yaml file in the project root is just a template as example.  
You need to override this with your own config file named "config.local.yaml". 

Then just start: 
```bash
py start.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)