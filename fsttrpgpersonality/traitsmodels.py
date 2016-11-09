from __future__ import print_function
from traits.api import *
from traitsui.api import *

from fsttrpgtables.models import Table
from fsttrpgcharloader.traitsmodels import CharacterName, list_of_actors
import utilities

quirks_table = Table('quirks')
disorders_table = Table('disorders')
phobias_table = Table('phobias')

prime_motivations_table = Table('prime_motivations')
most_valued_person_table = Table('valued_person')
most_valued_pos_table = Table('valued_posession')
feels_about_people_table = Table('valued_people')
inmodes_table = Table('inmodes')
exmodes_table = Table('exmodes')
clothes_table = Table('clothes')
hair_table = Table('hair')
affections_table = Table('affections')


class Phobias(HasTraits):
    phobias = List(editor=CheckListEditor(values=phobias_table.results(), cols=6))
    random_phobia = Button()

    traits_view = View(
        Item('phobias'),
        Item('random_phobia', show_label=False)
    )

    def _random_phobia_fired(self):
        self.phobias = phobias_table.multiple_randoms(1, 1)


class Disorders(HasTraits):
    disorders = List(editor=CheckListEditor(values=disorders_table.results(), cols=3))
    random_disorder = Button()

    def _random_disorder_fired(self):
        self.disorders = disorders_table.multiple_randoms(1, 1)

    view = View(
        Item('disorders', style='custom'),
        Item('random_disorder', show_label=False)
    )


class Quirks(HasTraits):
    quirks = List(editor=CheckListEditor(values=quirks_table.results(), cols=3))
    random_quirks = Button()

    def _random_quirks_fired(self):
        self.quirks = quirks_table.multiple_randoms(1, 3)

    view = View(
        Item('quirks', style='custom'),
        Item('random_quirks', show_label=False)
    )


class Hair(HasTraits):
    hairstyles = List(editor=CheckListEditor(values=hair_table.results(), cols=2))
    random_hairstyle = Button()

    def _random_hairstyle_fired(self):
        self.hairstyles = hair_table.multiple_randoms(1, 1)

    view = View(
        Item('hairstyles', style='custom'),
        Item('random_hairstyle', show_label=False)
    )


class Clothes(HasTraits):
    clothes = List(editor=CheckListEditor(values=clothes_table.results(), cols=2))
    random_clothes = Button()

    def _random_clothes_fired(self):
        self.clothes = clothes_table.multiple_randoms(1, 1)

    view = View(
        Item('clothes', style='custom'),
        Item('random_clothes', show_label=False)
    )


class Affections(HasTraits):
    affections = List(editor=CheckListEditor(values=affections_table.results(), cols=2))
    random_affection = Button()

    def _random_affection_fired(self):
        self.affections = affections_table.multiple_randoms(1, 1)

    view = View(
        Item('affections', style='custom'),
        Item('random_affection', show_label=False)
    )


class Personality(HasTraits):
    prime_motivation = Enum(prime_motivations_table.results())
    most_valued_person = Enum(most_valued_person_table.results())
    most_valued_posession = Enum(most_valued_pos_table.results())
    how_feels_about_most_people = Enum(feels_about_people_table.results())
    inmode = Enum(inmodes_table.results())
    exmode = Enum(exmodes_table.results())
    quirks = Instance(Quirks, ())
    disorders = Instance(Disorders, ())
    phobias = Instance(Phobias, ())
    hairstyle = Instance(Hair, ())
    clothes = Instance(Clothes, ())
    affections = Instance(Affections, ())

    random_motivation = Button()
    random_valued_person = Button()
    random_posession = Button()
    random_feels = Button()
    random_inmode = Button()
    random_exmode = Button()

    random_all = Button()


    def _random_motivation_fired(self):
        self.prime_motivation = prime_motivations_table.random_result()

    def _random_valued_person_fired(self):
        self.most_valued_person = most_valued_person_table.random_result()

    def _random_posession_fired(self):
        self.most_valued_posession = most_valued_pos_table.random_result()

    def _random_feels_fired(self):
        self.how_feels_about_most_people = feels_about_people_table.random_result()

    def _random_inmode_fired(self):
        self.inmode = inmodes_table.random_result()

    def _random_exmode_fired(self):
        self.exmode = exmodes_table.random_result()

    def _random_all_fired(self):
        self.prime_motivation = prime_motivations_table.random_result()
        self.most_valued_person = most_valued_person_table.random_result()
        self.most_valued_posession = most_valued_pos_table.random_result()
        self.how_feels_about_most_people = feels_about_people_table.random_result()
        self.inmode = inmodes_table.random_result()
        self.exmode = exmodes_table.random_result()
        self.quirks.quirks = quirks_table.multiple_randoms(1, 3)
        self.phobias.phobias = phobias_table.multiple_randoms(1, 1)
        self.hairstyle.hairstyles = hair_table.multiple_randoms(1, 1)
        self.clothes.clothes = clothes_table.multiple_randoms(1, 1)
        self.affections.affections = affections_table.multiple_randoms(1, 1)





    traits_view = View(
        HGroup(
            Group(
                Item('prime_motivation'),
                Item('most_valued_person'),
                Item('most_valued_posession'),
                Item('how_feels_about_most_people'),
                Item('inmode'),
                Item('exmode'),
                HGroup(
                    Group(
                        Item('quirks'),
                        Item('disorders')

                    ),
                    Group(
                        Item('hairstyle'),
                        Item('clothes')

                    ),
                    Group(
                        Item('affections'),
                        Item('phobias'),
                    )
                )
            ),
            Group(
                Item('random_motivation', show_label=False),
                Item('random_valued_person', show_label=False),
                Item('random_posession', show_label=False),
                Item('random_feels', show_label=False),
                Item('random_inmode', show_label=False),
                Item('random_exmode', show_label=False)
            )
        ),
        Item('random_all', show_label=False)
    )


class Standalone(HasTraits):
    character_name = Instance(CharacterName, ())
    personality = Instance(Personality, ())
    upload = Button()

    view = View(
        Item('character_name', style='custom', show_label=False),
        Item('personality', style='custom', show_label=False),
        Item('upload', show_label=False)
    )

    def _character_name_default(self):
        return CharacterName(name_change_handler=self.load_personality)

    def load_personality(self):

        name = self.character_name.name.name
        role = self.character_name.role
        # print(str(list_of_actors.actors))
        loaded_personality = list_of_actors.get_optional_value(name, 'personality')
        if loaded_personality:
            try:
                self.personality.prime_motivation = loaded_personality['motivation']
                self.personality.most_valued_person = loaded_personality['valued_person']
                self.personality.most_valued_posession = loaded_personality['valued_posession']
                self.personality.how_feels_about_most_people = loaded_personality['feels_about_people']
                self.personality.inmode = loaded_personality['inmode']
                self.personality.exmode = loaded_personality['exmode']
                self.personality.quirks.quirks = loaded_personality['quirks']
                self.personality.phobias.phobias = loaded_personality['phobias']
                self.personality.hairstyle.hairstyles = loaded_personality['hair']
                self.personality.clothes.clothes = loaded_personality['clothes']
                self.personality.affections.affections = loaded_personality['affections']
                self.personality.disorders.disorders = loaded_personality['disorders']
            except Exception as e:
                print('failed to load valid personality')
                print(str(e))

    def _upload_fired(self):
        utilities.save_character_info(role=self.loader.role, name=self.loader.selection,
                                      prime_motivation=self.prime_motivation, m_valued_person=self.most_valued_person,
                                      m_valued_posession=self.most_valued_posession,
                                      feels_about_people=self.how_feels_about_most_people, inmode=self.inmode,
                                      exmode=self.exmode, quirks=self.quirks.quirks, phobias=self.phobias.phobias,
                                      disorders=self.disorders.disorders, hair=self.hairstyle.hairstyles,
                                      clothes=self.clothes.clothes, affections=self.affections.affections)


if __name__ == '__main__':
    st = Standalone()
    st.configure_traits()
