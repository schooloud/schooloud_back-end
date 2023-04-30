from schooloud.model.project import Project


class ProjectController:
    def __init__(self):
        pass

    def get_project(self, projectId):
        project = Project.query.filter(Project.projectId == projectId).one()
        project_dict = {
            'isDeleted': project.isDeleted,
            'name': project.name,
            'instanceNum': project.instanceNum,
            'cpu': project.cpu,
            'memory': project.memory,
            'storage': project.storage,
            'createdAt': project.createdAt,
            'endAt': project.endAt,
        }
        return project_dict
