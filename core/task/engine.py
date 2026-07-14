from core.task.action import Action


class TaskEngine:


    def create_task(self, command):

        tasks = []


        command = command.lower()


        if "buka" in command:

            tasks.append(
                Action(
                    "open",
                    {
                        "url": command
                    }
                )
            )


        elif "cari" in command:

            tasks.append(
                Action(
                    "search",
                    {
                        "keyword": command
                    }
                )
            )


        else:

            tasks.append(
                Action(
                    "open",
                    {
                        "url": command
                    }
                )
            )


        return tasks