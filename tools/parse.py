class Parse:
    def __init__(self, file_path, parser):
        self.path = file_path
        self.type = file_path.split('.')[-1]
        self.parser = parser
        print(self.path, self.type)

    def __enter__(self):
        return self.parser(self.path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
