import pathlib
from dotenv import load_dotenv
from sql.database import Database

root_dir = pathlib.Path(__file__).parent


def create_db():
    db = Database()
    query = ("create table config_global ("
             "bot_token varchar(100),"
             "admins_global LONGTEXT"
             ");")

    db.execute(query)

    print("Created global config table")

    query = """create table config_guilds
        (
            id                    int auto_increment,
            guild_id              integer null,
            guild_captcha_channel int     null,
            constraint config_guilds_pk
                primary key (id)
        );
    """

    db.execute(query)

    db.commit()

    print("Created guild config table")

    bot_token = input("Bot token please: ")

    sql = "insert into config_global (bot_token, admins_global) values (%(token)s, %(admins)s)"

    db.execute(sql, {"token": bot_token, "admins": ""})

    db.close()


if __name__ == '__main__':
    load_dotenv()
    create_db()
