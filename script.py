import csv
import datetime
import logging

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

logger = logging.getLogger("AzureDevOpsMetrics")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

class AzureDevOpsMetrics:
    def __init__(self, personal_access_token, organization_url):
        self.personal_access_token = personal_access_token
        self.organization_url = organization_url
        self.credentials = BasicAuthentication('', personal_access_token)
        self.connection = Connection(base_url=organization_url, creds=self.credentials)
        self.project_client = self.connection.clients.get_core_client()
        self.repo_client = self.connection.clients.get_git_client()
        self.data = []

    def get_projects(self):
        return self.project_client.get_projects()

    def get_repositories(self, project_id):
        return self.repo_client.get_repositories(project=project_id)

    def get_items(self, repository_id, path, version_descriptor):
        return self.repo_client.get_items(repository_id=repository_id, scope_path=path, recursion_level='full')

    def get_item_content(self, repository_id, path, version_descriptor=None):
        return self.repo_client.get_item_content(repository_id=repository_id, path=path)

    def count_lines(self, content_bytes):
        content_text = content_bytes.decode('utf-8')
        return content_text.count('\n')

    def analyze_repositories(self):
        for project in self.get_projects():
            project_name = project.name
            logger.debug(f"Get information about project {project_name}")
            for repo in self.get_repositories(project.id):
                repo_name = repo.name
                logger.debug(f"Get information about repo {repo_name}")
                default_branch = repo.default_branch

                if default_branch:
                    total_lines = 1
                    items = self.get_items(repository_id=repo.id, path="/", version_descriptor=default_branch)

                    for item in items:
                        if not item.is_folder:
                            content = self.get_item_content(repository_id=repo.id, path=item.path, version_descriptor=default_branch)
                            content_bytes = b"".join([chunk for chunk in content])
                            total_lines += self.count_lines(content_bytes)

                    logger.debug(f"Total number of lines: {total_lines}")
                    self.data.append([project_name, repo_name, default_branch, total_lines])

    def save_metrics_to_csv(self):
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        filename = f'report_{timestamp}.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome do Projeto', 'Repositório', 'Branch default', 'Número de linhas'])
            writer.writerows(self.data)
        logger.info(f"Relatório salvo em {filename}")


def main():
    # Definindo as credenciais de acesso ao azure devops
    personal_access_token = 'SEU_TOKEN_DE_ACESSO_PESSOAL'
    organization_url = 'https://dev.azure.com/sua-organizacao'

    logger.info("Starting...")

    # Criando uma instância do AzureDevOpsMetrics
    azure_devops_metrics = AzureDevOpsMetrics(personal_access_token, organization_url)

    # Analisando os repositórios e coletando as métricas
    azure_devops_metrics.analyze_repositories()

    # Salvando as métricas em um arquivo CSV
    azure_devops_metrics.save_metrics_to_csv()


if __name__ == '__main__':
    main()
