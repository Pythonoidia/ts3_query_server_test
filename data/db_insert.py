import sqlite3


class DbInteractions(object):
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def Insert_channel_name(self, server_id, id_num, channel_name):
        sql_string_channel_name = "INSERT INTO channel_properties VALUES"\
                "({server_id}, {id_num}, 'channel_name', '{channel_name}'"
        sql_command_channel_name = sql_string_channel_name.format(server_id=server_id, id_num=id_num,
                channel_name=channel_name)
        self.cursor.execute(sql_command_channel_name)

        try:
            self.connection.commit()
            print("commiting")
        except sqlite3.Error as e:
            print('failed to commit data, Error: {}'. format(e.args[0]))


def main():
    db = DbInteractions("ts3server.sqlitedb")
    db.Insert_channel_name(1, 1, 'bazunga')

if __name__ == "__main__":
    main()
