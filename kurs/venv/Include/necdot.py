# -*- coding: utf-8 -*-

import random

def get(vk_session, id_group,vk):
    try:

        max_num = vk.nekdot.get(owner_id=id_group, album_id='wall', count=0)['count']
        num = random.randint(1, max_num)
        pictures = vk.nekdot.get(owner_id=str(id_group), album_id='wall', count=1, offset=num)['items']
        buf = []
        for element in pictures:
            buf.append('photo' + str(id_group) + '_' + str(element['id']))
        print(buf)
        attachment = ','.join(buf)
        print(type(attachment))
        print(attachment)
        return attachment
    except:
        return get(vk_session, id_group, vk)