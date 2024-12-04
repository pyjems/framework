import importlib


class RouteLoader:
    def __init__(self):
        self._routes_cache = {}

    def load_routes(self, loader: str):

        if loader in self._routes_cache:
            return self._routes_cache[loader]

        try:
            module = importlib.import_module(loader)

            self._routes_cache[loader] = module

            return module
        except Exception as e:
            raise e
