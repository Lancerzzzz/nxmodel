#!/usr/bin/python3

# -*- coding: utf-8 -*-
# @Time    : 5/17/2019 3:44 PM
# @Author  : Lxz
from swmodel.topsystem import TopSystem


class InterfaceEntity(TopSystem.TopSystem):

    def __init__(self, **conf_param):
        self.payload = {}
        self.children = []
        self.att = {}
        self.Configurable_Properties = {
        }
        self.Internal_Properties = {
            "childAction": "",
            "descr": "",
            "dn": "sys/intf",
            "modTs": "",
            "persistentOnReload": "",
            "status": ""
        }
        self.conf_param = conf_param

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
            "interfaceEntity": {
            }
        }
        self.local_payload_children(**pd)
        self.payload["interfaceEntity"].update(self.children)
        return super().update_payload(self.payload)

    def get_final_pd(self):
        pass
