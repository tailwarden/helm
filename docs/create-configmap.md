## Create a ConfigMap manifest file with the profile credentials data for each account.<a name="create-service-account-iam-role"></a>

1. Add the configmap.yaml file the the `/templates` folder in the root of the repository.

   ```
    apiVersion: v1
    kind: ConfigMap
    data:
    credentials: |-
        [ADMIN-account]
        region = ${REGION}
        role_arn = arn:aws:iam::${ADMIN_AWS_ACCOUNT_ID}:role/${ROLE_NAME}
        web_identity_token_file = /var/run/secrets/eks.amazonaws.com/serviceaccount/token

        [DEV-account]
        region = ${REGION}
        role_arn = arn:aws:iam::${DEV_AWS_ACCOUNT_ID}:role/${ROLE_NAME}
        source_profile = ADMIN-account
        role_session_name = komiser_session
    metadata:
    annotations:
        meta.helm.sh/release-name: ${RELEASE_NAME}
        meta.helm.sh/release-namespace: ${NAMESPACE}
    labels:
        app.kubernetes.io/managed-by: Helm
    name: aws-configmap
    namespace: ${NAMESPACE}
   ```