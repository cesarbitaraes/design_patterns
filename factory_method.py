from abc import ABCMeta, abstractmethod


# Product
class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


# ConcreteProduct
class PersonalSection(Section):
    def describe(self):
        print("Personal Section")


# ConcreteProduct
class AlbumSection(Section):
    def describe(self):
        print("Album Section")


# ConcreteProduct
class PatentSection(Section):
    def describe(self):
        print("Patent Section")


# ConcreteProduct
class PublicationSection(Section):
    def describe(self):
        print("Publication Section")


# Creator
class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    # factory_method()
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_sections(self, section):
        self.sections.append(section)


# ConcreteCreator
class Linkedin(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(PatentSection())
        self.add_sections(PublicationSection())


# ConcreteCreator
class Facebook(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())


if __name__ == "__main__":
    profile_type = input("Which profile you'd like to create? Linkedin or Facebook: ")
    profile = eval(profile_type)()
    print("Creating profile...", type(profile).__name__)
    print("Profile has sections: ", profile.get_sections())

# Proporciona flexibilidade e deixa o código genérico.
# Há baixo acoplamento, pois o código que cria o objeto está separado do código que o utiliza.