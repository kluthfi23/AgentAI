from core.task.action import Action


class TaskEngine:

    def create_task(self, command):

        tasks = []

        command = command.lower().strip()

        # Pisahkan berdasarkan kata "lalu"
        parts = [p.strip() for p in command.split("lalu")]

        for part in parts:

            if part.startswith("buka "):

                url = part.replace("buka ", "", 1).strip()

                tasks.append(
                    Action(
                        "open",
                        {
                            "url": url
                        }
                    )
                )

            elif part.startswith("cari "):

                keyword = part.replace("cari ", "", 1).strip()

                tasks.append(
                    Action(
                        "search",
                        {
                            "keyword": keyword
                        }
                    )
                )

            elif "screenshot" in part:

                tasks.append(
                    Action(
                        "screenshot"
                    )
                )

            elif "download" in part:

                tasks.append(
                    Action(
                        "download"
                    )
                )

            else:

                tasks.append(
                    Action(
                        "unknown",
                        {
                            "command": part
                        }
                    )
                )

        return tasks