#!/usr/bin/python3

# -*- coding: utf-8 -*-
# @Time    : 5/23/2019 3:44 PM
# @Author  : Lxz
from swmodel.topsystem.interfaceEntity.l1PhysIf import l1PhysIf


class conf_trunk():

    def __init__(self, username, passwd, url, eth, mode, trunkvlans):

        self.usname = username
        self.passwd = passwd
        self.url = url

        self.map = [
            {"l1PhysIf":
                {
                "id": eth,
                "mode": mode,
                "trunkvlans": trunkvlans

                }
            }
        ]
        self.payload = self.get_payload()


    def send(self):

        return True

    def get_payload(self):
        ptrunk = l1PhysIf.l1PhysIf(*self.map).get_final_pd()

        return ptrunk.get_final_pd

