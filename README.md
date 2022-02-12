
```sh
python3 -m venv venv
source venv/bin/activate

pip install boto3

pip freeze > requirements.txt
```

```sh
serverless deploy --region us-west-2

serverless plugin install -n serverless-python-requirements 
```