from diagrams import Diagram
from diagrams.aws.compute import EC2

with Diagram("nomad-aws", show=False, direction="TB"):
            EC2("nomad-server") - EC2("nomad-client")
