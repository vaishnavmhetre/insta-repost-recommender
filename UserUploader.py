from flask import Flask

from DB.DBHelper import DBHelper
from DB.Models import Post, ClientUser
from Instagram import Instantiator
from Instagram import User as InstaUser
from time import sleep
import random

clients = [
    "romaniuk.eu",
    "charlinemouton",
    "satis.faction.st",
    "rue_altiay",
    "annejuliahagen",
    "bengal_gypsy",
    "sooprettiee",
    "samiraxmalika",
    "gabrieljackowski",
    "theemelly",
    "juli_daviss",
    "rinabeautly",
    "freelyfashion01",
    "kimberly_bru",
    "virginia_konopka",
    "imdollka",
    "untroddenpath_",
    "alexandra_and_borys_alexander",
    "annaherbstkoenig",
    "deepankara",
    "marta.ziobro",
    "madina_lolaeva",
    "stefanie.auinger",
    "magdalencja_",
    "carmenthornton.thorntonlaw",
    "cladia.sk",
    "nicole_van_dam",
    "tomek_piotrowskii",
    "whiteprince96",
    "itsabla",
    "lindalic0us",
    "ritalubrano",
    "jfpazphoto",
    "endorfinyalexy",
    "garderobelove",
    "walalmorimc",
    "rachelturzer",
    "meleerah",
    "james.v1",
    "asiabrach",
    "missglamzy",
    "laurabccom",
    "laurenhudson17",
    "kit_stanwood",
    "crystalstasolla",
    "turnitinsideout",
    "alexsaibrahim",
    "lacey_spalding",
    "shruti_2611",
    "sashawlt",
    "shlastreet",
    "the_tanvi_sinha",
    "sheheartstealer",
    "diiyalamba",
    "madame_marcelline",
    "tecnograph_",
    "ankycutyee",
    "madcatfashion",
    "hoinkis",
    "stalblue_",
    "beguilingstar",
    "rita_shamoun",
    "_bradw_official",
    "daniel_lott_",
    "jitesh005",
    "shreya_rao_k",
    "joanfradera",
    "vishalchaudary24",
    "monaschafnitzl",
    "mohitmalik1113",
    "charlesandron",
    "mandeepgujjar_",
    "antoniaelena.official",
    "pixelpune",
    "haleyoconnor7",
    "sandraobeid12",
    "farahcharaf",
    "fashio_nistha",
    "nehaa141",
    "robin_singh_official",
    "minalpatilofficial",
    "linda_lime",
    "modelonamission",
    "jona_borges",
    "tharina_botes",
    "akanshabhargavaa",
    "jasperrebel",
    "dianabstyle",
    "twojastylistkamarta",
    "princessyilin",
    "niklasrill",
    "shivani_midda",
    "franceska.bello",
    "wass_rzk",
    "lovamoi",
    "ilianatzikas",
    "chrisb1903",
    "koogallove",
    "aceharper",
    "dimpisasanghvi_ws",
    "nealmhair",
    "chahatmalik",
    "luke.baldman",
    "file_with_fashion",
    "zaitsevaworld",
    "youclement",
    "deepikabutola",
    "rits_badiani",
    "theglamorous_chic",
    "lexandthecity___",
    "arosegoldn",
    "silkehajunga",
    "mariusz_janecki",
    "fouadyouri",
    "andreakerbuski",
    "_maglu_",
    "taciticphotography",
    "_kaliver",
    "ishwetarathore",
    "alpha_and_omegaphotography",
    "talyhassan",
    "saraonsiofficial",
]

DATABASE = {
    'name': 'storage/storage.db',
    'engine': 'peewee.SqliteDatabase',
}

INSTAGRAM_CONFIG = {
    'username': 'fashionstreetig',
    'password': "mahajan@123"
}

db = None

DEBUG = True
SECRET_KEY = 'ssshhhh'


def initApp():
    global db

    app = Flask(__name__)
    app.config.from_object(__name__)

    # instantiate the db wrapper
    db = DBHelper(app).db


if __name__ == "__main__":

    initApp()

    Post.create_table(fail_silently=True)
    ClientUser.create_table(fail_silently=True)

    api = Instantiator.getApiInstance(INSTAGRAM_CONFIG['username'], INSTAGRAM_CONFIG['password'])

    for username in clients:
        print("Assessing ClientUser {}".format(username))
        sleep(random.randint(200, 800)/1000)
        user = InstaUser.getUserFromUsername(api, username)
        if 'user' in dict(user).keys():
            user = user['user']
            try:
                print("Checking existence of ClientUser \"{}\"".format(username))
                ClientUser.get(ClientUser.pk == user['pk'])
                print("Already stored ClientUser \"{}\"".format(username))
            except ClientUser.DoesNotExist as e:
                print("Creating ClientUser \"{}\"".format(username))
                created_user = ClientUser.create(pk=user['pk'], username=user['username'])
