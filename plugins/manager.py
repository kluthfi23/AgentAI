from plugins.generic import GenericPlugin
from plugins.google import GooglePlugin
from plugins.youtube import YouTubePlugin


class PluginManager:

    def load(self, url):

        url = url.lower()

        if "youtube" in url:
            return YouTubePlugin()

        if "google" in url:
            return GooglePlugin()

        return GenericPlugin()