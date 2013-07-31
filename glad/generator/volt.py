import glad.generator
import os.path


class VoltGenerator(Generator):
    def generate_loader(self, api, version):
        raise NotImplementedError

    def generate_enums(self, api, version, enums):
        raise NotImplementedError

    def generate_functions(self, api, version, functions):
        raise NotImplementedError

    def generate_extension(self, api, version, ext):
        raise NotImplementedError