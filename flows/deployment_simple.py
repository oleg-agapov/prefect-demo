from etl_github_data import github_pipeline
from prefect.deployments import Deployment

deployment = Deployment.build_from_flow(
    flow=github_pipeline,
    name='Deployment Simple',
    parameters={
        'date': '2015-01-01',
        'hour': 1
    }
)
deployment.apply()
