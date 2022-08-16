## Mount the ConfigMap onto the deployment in order to be able to load the pod with the requiste AWS credentials.<a name="create-service-account-iam-role"></a>

1. Make sure not to change the mount path or internal volume path, paths should match the example below.
2. Add the `command: ["--multiple"]` to the container to allow a multi account setup

   ```
    apiVersion: apps/v1 
    kind: Deployment 
    metadata: 
    name: komiser
    spec:
    selector: 
        matchLabels: 
        app: komiser
    template: 
        metadata: 
        name: komiser
        labels: 
            app: komiser
        spec:
        serviceAccountName: komiser
        containers: 
            - name: {{ .Chart.Name }}
            image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
            imagePullPolicy: {{ .Values.image.pullPolicy }}
            command: ["--multiple"]
            env:
                - name: AWS_DEFAULT_REGION
                value: "{{ .Values.aws.region }}"
                - name: AWS_CONFIG_FILE
                value: /root/.aws/credentials
            volumeMounts:
            - name: test-volume
                mountPath: /root/.aws/
        volumes:
        - name: test-volume
            configMap:
            name: aws-configmap
   ```