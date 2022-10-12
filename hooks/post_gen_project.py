import os
import shutil

project_name = "{{cookiecutter.project_name}}"
current_cloud = "{{cookiecutter.cloud}}"
cloud_specific_paths = {
    "azure": [
        os.path.join(".github", "workflows", "scripts", "generate-aad-token.sh"),
        os.path.join(".mlops-setup-scripts", "cicd", "main-azure.tf"),
        os.path.join(".mlops-setup-scripts", "terraform", "main-azure.tf"),
    ],
    "aws": [
        os.path.join(".mlops-setup-scripts", "cicd", "main-aws.tf"),
        os.path.join(".mlops-setup-scripts", "terraform", "main-aws.tf"),
    ],
}

for cloud, paths in cloud_specific_paths.items():
    if cloud != current_cloud:
        for path in paths:
            os.remove(path)

cicd_platform = "{{cookiecutter.cicd_platform}}"
cicd_specific_paths = {
    "gitHub": [
        os.path.join(".github", "workflows"),
    ],
    "azureDevOpsServices": [
        os.path.join(".azure", "devops-pipelines"),
    ],
}

for cicd, paths in cicd_specific_paths.items():
    if cicd != cicd_platform:
        for path in paths:
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
            else:
                raise ValueError(f"{path} is not a file of a dir.")


# Remove test files
test_paths = ["_params_testing_only.txt"]
if project_name != "27896cf3-bb3e-476e-8129-96df0406d5c7":
    for path in test_paths:
        os.remove(path)


readme_path = os.path.join(os.getcwd(), "README.md")
print(
    f"Finished generating ML project. See the generated README at {readme_path} for next steps!"
)
