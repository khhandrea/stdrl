class DotDict(dict):
    def __getattr__(self, name):
        return self[name]