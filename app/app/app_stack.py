import aws_cdk.aws_eks as eks
from aws_cdk import Stack, CfnParameter
from constructs import Construct

class KomiserStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        cluster_name = CfnParameter(self, "EKSClusterName", type="String", description="The name of the Amazon EKS cluster where Komiser will be deployed.")

        # Create an EKS cluster
        cluster = eks.Cluster(self, cluster_name.to_string(), version=eks.KubernetesVersion.V1_25)

        # Deploy the Helm chart
        eks.HelmChart(self, "komiser", cluster=cluster, chart="komsier-chart", repository="https://github.com/tailwarden/helm.git")

