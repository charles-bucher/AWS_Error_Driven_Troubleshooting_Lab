import pytest
import os


@pytest.fixture
def aws_credentials():
    """Mock AWS credentials for testing"""
import os
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'


@pytest.fixture
def mock_config():
    """Mock configuration for tests"""
    return {
        'region': 'us-east-1',
        'instance_type': 't2.micro',
        'ami_id': 'ami-12345678'
    }
