## Create policy and attach it to the ADMIN role to be able to assume the target DEV role.<a name="create-service-account-iam-role"></a>

1. Choose a name for the policy  i.e "assume-target-account-role-policy".

   ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "sts:AssumeRole",
                "Resource": "arn:aws:iam::${DEV_ACCOUNT_ID}:role/${ROLE_NAME}"
            }
        ]
    }
   ```
