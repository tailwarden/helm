import aws_cdk.aws_eks as eks
from aws_cdk import core
from aws_cdk.lambda_layer_kubectl import KubectlLayer

class KomiserStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an EKS cluster
        cluster = eks.Cluster(self, "KomiserTestCluster", version=eks.KubernetesVersion.of(version="v1_25"))

        # Deploy the Helm chart from the my-chart directory
        eks.HelmChart(self, "komiser", cluster=cluster, chart="komsier-chart", repository="https://github.com/tailwarden/helm.git")

