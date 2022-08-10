## Create a Trust Relationship and attach it to the Dev role to allow the ADMIN role to assume it.<a name="create-service-account-iam-role"></a>

1. Choose a name for the policy  i.e "assume-target-account-role-policy".

   ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "AWS": "arn:aws:iam::${ADMIN_ACCOUNT_ID}:role/${ROLE_NAME}"
                },
                "Action": "sts:AssumeRole",
                "Condition": {}
            }
        ]
    }
   ```