from fsttrpgtables.models import Table
import utilities


class TableValue(object):
    def __init__(self, source_table_name, random_method='single', random_min=1, random_max=1):
        super(TableValue, self).__init__()
        self.value = None
        self.source_table = Table(source_table_name)
        self.random_method = random_method
        self.random_min = random_min
        self.random_max = random_max

    def get_random(self, return_as_option=False):
        if self.random_method is 'multiple':
            self.value = self.source_table.multiple_randoms(min=self.random_min, max=self.random_max)
        else:
            if return_as_option:
                self.value = self.source_table.random_option()
            else:
                self.value = self.source_table.random_result()
        return self.value


class Personality(object):
    def __init__(self):
        super(Personality, self).__init__()
        self.prime_motivation = TableValue(source_table_name='prime_motivations')
        self.most_valued_person = TableValue(source_table_name='valued_person')
        self.most_valued_posession = TableValue(source_table_name='valued_posession')
        self.how_feels_about_most_people = TableValue(source_table_name='valued_people')
        self.inmode = TableValue(source_table_name='inmodes')
        self.exmode = TableValue(source_table_name='exmodes')
        self.quirks = TableValue(source_table_name='quirks', random_method='multiple', random_min=1, random_max=3)
        self.disorders = TableValue(source_table_name='disorders', random_method='multiple')
        self.phobias = TableValue(source_table_name='phobias', random_method='multiple')
        self.hairstyle = TableValue(source_table_name='hair', random_method='multiple')
        self.clothes = TableValue(source_table_name='clothes', random_method='multiple')
        self.affections = TableValue(source_table_name='affections', random_method='multiple')

    def assign_random_to_field(self, field_name):
        try:
            field = self.__getattribute__(field_name)
            return field.get_random()
        except KeyError:
            print('no such field')

    def upload_to_aws(self, role, actor_name):
        pm = self.prime_motivation.value
        mvper = self.most_valued_person.value
        mvpos = self.most_valued_posession.value
        fap = self.how_feels_about_most_people.value
        inm = self.inmode.value
        exm = self.exmode.value
        qui = self.quirks.value
        pho = self.phobias.value
        dis = self.disorders.value
        hai = self.hairstyle.value
        clo = self.clothes.value
        aff = self.affections.value
        utilities.save_character_info(role=role, name=actor_name, prime_motivation=pm, m_valued_person=mvper,
                                      m_valued_posession=mvpos, feels_about_people=fap, inmode=inm, exmode=exm,
                                      quirks=qui, phobias=pho, disorders=dis, hair=hai, clothes=clo, affections=aff)
