

class RawManipulation(object):
    def __init__(self, filename):
        self.filename = filename

    def adding_channel(self, channel_name, channel_topic = "protected", channel_password, channel_number):
        '''
        Method responsible for putting data into sql initialization file
        INPUT:
            channel_name = name of channel that we want to add
            channel_topic = topic of channel, if we want to prevent huskar bot
            from deleting it you dont have to pass anything by argument
            channel_password = password of channel
            channel_number = number of channel, its important because under
            exact number channel will be stored locally in server files
        IMPORTANT: channel_number value must be unique
        '''
        payload = []
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_name','{channel_name}');\n".format(channel_name=channel_name))
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_topic','{channel_topic}');\n".format(channel_topic=channel_topic))
        payload.append("INSERT_INTO " + '"channel_properties"' + " VALUES(1,1,'channel_description','This is channel created by Python');")
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_password',{channel_password});".format(channel_password=channel_password))
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_codec','4');")
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_codec_quality','6');")
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_max_clients', '-1');")
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_max_familyclients','-1');")
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_order','0');")
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_flag_permanent','1');")
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_flag_semi_permanent','0');")
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_flag_password','1');")
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_codec_latency_factor','0');")
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_codec_is_unencrypted','1');")
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_security_salt','');")
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_flag_maxclients_unlimited','1');")
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_flag_maxfamilyclients_unlimited','1');")
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_flag_maxfamilyclients_inherited','0');")
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_filepath','files/virtualserver_1/channel_{channel_number}');".format(channel_number))
        payload.append("INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'channel_name_phonetic','');")
        return payload

    def file_writing(self, payload):
        for command in payload:
            with open(self.filename, encoding = "ISO-8859-1", mode='a') as file:
                self.data = file.write(command)
        print(self.data)


def main():
    raw = RawManipulation('ts3server.sqlitedb')
    #raw = RawManipulation('newfile')
    #print(raw.file_writing('bac'))
    print(raw.adding_channel('bleble','blabla'))


if __name__ == '__main__':
    main()
