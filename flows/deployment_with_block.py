from etl_github_data import github_pipeline
from prefect.deployments import Deployment
from prefect.filesystems import GitHub

github_block = GitHub.load('github-block')

deployment = Deployment.build_from_flow(
    flow=github_pipeline,
    name='Deployment Simple',
    parameters={
        'date': '2015-01-01',
        'hour': 1
    },
    storage=github_block,
)

deployment.apply()
