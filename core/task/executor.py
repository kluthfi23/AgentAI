class TaskExecutor:


    def execute(self, page, tasks):

        for task in tasks:


            print(
                f"[TASK] {task.action}"
            )


            if task.action == "open":

                url = task.data["url"]

                if not url.startswith("http"):

                    url = "https://" + url


                page.goto(url)



            elif task.action == "search":

                print(
                    "Search:",
                    task.data["keyword"]
                )