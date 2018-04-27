

class RawManipulation(object):
    def __init__(self, filename):
        self.filename = filename

    def adding_channel(self, channel_name, channel_password, channel_number, channel_topic='protected'):
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
        insert_string = "INSERT INTO " + '"channel_properties"' + " VALUES(1,1,'{channel_property}','{value}');" + '\n'
        payload = []
        payload.append(insert_string.format(channel_property='channel_name', value=channel_name))
        payload.append(insert_string.format(channel_property='channel_topic', value=channel_topic))
        payload.append(insert_string.format(channel_property='channel_description', value='This is channel created by Python'))
        payload.append(insert_string.format(channel_property='channel_password',value=channel_password))
        payload.append(insert_string.format(channel_property='channel_codec',value='4'))
        payload.append(insert_string.format(channel_property='channel_codec_quality',value='6'))
        payload.append(insert_string.format(channel_property='channel_max_clients',value='-1'))
        payload.append(insert_string.format(channel_property='channel_max_familyclients',value='-1'))
        payload.append(insert_string.format(channel_property='channel_order',value='0'))
        payload.append(insert_string.format(channel_property='channel_flag_permanent',value='1'))
        payload.append(insert_string.format(channel_property='channel_flag_semi_permanent',value='0'))
        payload.append(insert_string.format(channel_property='channel_flag_password',value='1'))
        payload.append(insert_string.format(channel_property='channel_codec_latency_factor',value='0'))
        payload.append(insert_string.format(channel_property='channel_codec_is_unencrypted',value='1'))
        payload.append(insert_string.format(channel_property='channel_security_salt',value=''))
        payload.append(insert_string.format(channel_property='channel_flag_maxclients_unlimited',value='1'))
        payload.append(insert_string.format(channel_property='channel_flag_maxfamilyclients_unlimited',value='1'))
        payload.append(insert_string.format(channel_property='channel_flag_maxfamilyclients_inherited',value='0'))
        payload.append(insert_string.format(channel_property='channel_filepath',value="files/virtualserver_1/channel_'{}'".format(channel_number)))
        payload.append(insert_string.format(channel_property='channel_name_phonetic',value=''))
        return payload

    def file_writing(self, payload):
        for command in payload:
            with open(self.filename, encoding = "ISO-8859-1", mode='a') as file:
                self.data = file.write(command)
        print(self.data)


def main():
    raw = RawManipulation('ts3server.sqlitedb')
    raw.file_writing(raw.adding_channel('cool_cat', 'cat123', '31'))


if __name__ == '__main__':
    main()
