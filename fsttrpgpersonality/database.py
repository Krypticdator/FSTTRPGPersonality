from fsttrpgcharloader.database import DBManager as ActorDBManager, Actor
from fsttrpgtables.db import DBManager as TableManager
from peewee import Model, SqliteDatabase, CharField, ForeignKeyField

personality_db = SqliteDatabase('personalities.db')


class BaseModel(Model):
    class Meta:
        database = personality_db


class CharacterPersonalityTrait(BaseModel):
    actor = ForeignKeyField(Actor, 'personalitytraits')
    trait_type = CharField()
    trait_name = CharField()

    @staticmethod
    def add_if_doesnt_exist(actor_role, actor_name, trait_type, trait_name):
        act = Actor.add_or_get(role=actor_role, name=actor_name)
        actor, created = CharacterPersonalityTrait.get_or_create(actor=act, trait_type=trait_type,
                                                                 trait_name=trait_name)
        if created:
            print('created new personality trait')
        else:
            print('this trait is already present')

    @staticmethod
    def get_all_traits(actor_role, actor_name):
        act = Actor.get(Actor.role == actor_role, Actor.name == actor_name)
        return CharacterPersonalityTrait.select().where(CharacterPersonalityTrait.actor == act)


class Personality(BaseModel):
    actor = ForeignKeyField(rel_model=Actor, related_name='personalities')
    prime_motivation = CharField()
    most_valued_person = CharField()
    most_valued_posession = CharField()
    feels_about_people = CharField()
    inmode = CharField()
    exmode = CharField()

    @staticmethod
    def add(actor_role, actor_name, prime_motivation, most_valued_person, most_valued_pos, feels_about_people,
            inmode, exmode, quirks, phobias, disorders, hairs, clothing, affections):
        act = Actor.add_or_get(role=actor_role, name=actor_name)
        personality, created = Personality.get_or_create(actor=act,
                                                         defaults={'prime_motivation': prime_motivation,
                                                                   'most_valued_person': most_valued_person,
                                                                   'most_valued_posession': most_valued_pos,
                                                                   'feels_about_people': feels_about_people,
                                                                   'inmode': inmode,
                                                                   'exmode': exmode})
        if created:
            for quirk in quirks:
                CharacterPersonalityTrait.add_if_doesnt_exist(actor_role=actor_role, actor_name=actor_name,
                                                              trait_type='quirk', trait_name=quirk)
            for phobia in phobias:
                CharacterPersonalityTrait.add_if_doesnt_exist(actor_role=actor_role, actor_name=actor_name,
                                                              trait_type='phobia', trait_name=phobia)

            for disorder in disorders:
                CharacterPersonalityTrait.add_if_doesnt_exist(actor_role=actor_role, actor_name=actor_name,
                                                              trait_type='disorder', trait_name=disorder)
            for hair in hairs:
                CharacterPersonalityTrait.add_if_doesnt_exist(actor_role=actor_role, actor_name=actor_name,
                                                              trait_type='hair', trait_name=hair)
            for cloth in clothing:
                CharacterPersonalityTrait.add_if_doesnt_exist(actor_role=actor_role, actor_name=actor_name,
                                                              trait_type='clothes', trait_name=cloth)
            for affection in affections:
                CharacterPersonalityTrait.add_if_doesnt_exist(actor_role=actor_role, actor_name=actor_name,
                                                              trait_type='affection', trait_name=affection)

    def get_personality_of(self, actor_role, actor_name):
        act = Actor.get(Actor.role == actor_role, Actor.name == actor_name)
        per = Personality.get(Personality.actor == act)
        traits = CharacterPersonalityTrait.get_all_traits(actor_role=actor_role, actor_name=actor_name)
        return {'personality': per, 'traits': traits}




class DBManager(object):
    def __init__(self):
        super(DBManager, self).__init__()
        self.tables_db_mgr = TableManager()
        self.actors_db_mgr = ActorDBManager()
        personality_db.connect()
        personality_db.create_tables([Personality, CharacterPersonalityTrait], True)
        self.personality_db = personality_db
        self.personalities_table = Personality()

    def __del__(self):
        personality_db.close()
