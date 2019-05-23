#!/usr/bin/python3

# -*- coding: utf-8 -*-
# @Time    : 5/17/2019 3:44 PM
# @Author  : Lxz


class TopSystem(object):

    def __init__(self, **conf_param):
        self.payload = {}
        self.children = []
        self.att = {}
        self.Configurable_Properties = {
            "dn": "sys",
            "name": "",
            "persistentOnReload": ""
        }
        self.Internal_Properties = {
            "serial": "",
            "status": "",
            "systemUpTime": "",
            'childAction': '',
            "currentTime": "",
            "modTs": ""
        }
        self.conf_param = conf_param
        self.children=[]
        pass



    def local_payload_att(self):
        for i in self.conf_param.keys():
            if i not in self.Configurable_Properties.keys():
                return {}
        self.att = {
            "attributes": self.conf_param
        }
        return self.att

    def local_payload_children(self, pd):
        self.children = {
            "children": [pd]
        }

    def update_payload(self, pd):
        self.payload = {
            "topSystem": {
            }
        }
        self.local_payload_children(**pd)
        self.payload["topSystem"].update(self.children)
        print(self.payload)
        return self.payload

    def get_final_pd(self):
        pass

