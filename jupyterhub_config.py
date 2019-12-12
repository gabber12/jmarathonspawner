import os

c.JupyterHub.spawner_class = 'jmarathonspawner.MarathonSpawner'

c.MarathonSpawner.image = 'jupyterhub/singleuser'
c.MarathonSpawner.cmd = 'jupyterhub-singleuser --ip=0.0.0.0 --port=8000'
c.MarathonSpawner.app_prefix = 'jupyter' # AppName Template: {app_prefix}/{user}-{server_name}
c.MarathonSpawner.marathon_host = 'http://leader.mesos:8080' 
c.MarathonSpawner.ports = [8000] #Ports to expose
c.MarathonSpawner.mem_limit = '2G'
c.MarathonSpawner.cpu_limit = 1
c.MarathonSpawner.network_mode = 'BRIDGE'
c.MarathonSpawner.hub_ip_connect = os.environ.get("PUBLIC_HOST")
c.MarathonSpawner.hub_port_connect = os.environ.get("PUBLIC_PORT")
c.MarathonSpawner.custom_env = [{"JUPYTERHUB_API_URL":"http://"+os.environ.get("PUBLIC_HOST")+":"+os.environ.get("PUBLIC_PORT")+/hub/api" }]


c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
