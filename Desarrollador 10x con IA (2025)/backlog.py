from models import WorkItem

def parsear_backlog(json_data: dict, sprint_nombre: str) -> list[WorkItem]:
    items = []

    for epic in json_data["epics"]:
        items.append(
            WorkItem(
                id=epic["id"],
                work_item_type="Epic",
                title=epic["title"],
                description=epic["description"],
                state="New",
                iteration_path=sprint_nombre,
                parent=None
            )
        )

        for us in epic["user_stories"]:
            items.append(
                WorkItem(
                    id=us["id"],
                    work_item_type="User Story",
                    title=us["title"],
                    description=us["description"],
                    state="New",
                    iteration_path=sprint_nombre,
                    parent=epic["id"]
                )
            )

            for task in us["tasks"]:
                items.append(
                    WorkItem(
                        id=task["id"],
                        work_item_type="Task",
                        title=task["title"],
                        description=task["description"],
                        state="New",
                        iteration_path=sprint_nombre,
                        parent=us["id"]
                    )
                )

    return items