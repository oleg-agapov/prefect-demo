from prefect.filesystems import GitHub

repo = 'https://github.com/oleg-agapov/prefect-demo'

github_block = GitHub(
    name="github-block",
    repository=repo
)

github_block.save('github-block', overwrite=True)
