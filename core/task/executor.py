class TaskExecutor:

    def execute(self, page, plugin, tasks):

        for task in tasks:

            action = task.action

            data = task.data

            print(f"[EXECUTOR] {action}")

            if action == "open":

                plugin.open(
                    page,
                    data["url"]
                )

            elif action == "search":

                plugin.search(
                    page,
                    data["keyword"]
                )

            elif action == "screenshot":

                plugin.screenshot(page)

            elif action == "download":

                plugin.download(page)

            else:

                print(
                    f"[WARNING] Unknown action: {action}"
                )