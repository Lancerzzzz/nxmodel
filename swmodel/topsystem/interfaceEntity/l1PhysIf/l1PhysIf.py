from swmodel.topsystem.interfaceEntity import interfaceEntity
import json

class l1PhysIf(interfaceEntity.InterfaceEntity):
    def __init__(self, **conf_param):
        self.payload = {}
        self.children = []
        self.att = {}
        self.Configurable_Properties = {
            "dn": "sys/intf/phys-[eth1/1]",
            "rn": "phys-[eth1/1]",
            "FECMode": "auto",
            "accessVlan": "vlan-1",
            "adminSt": "up",
            "autoNeg": "on",
            "beacon": "off",
            "bw": "default",
            "controllerId": "",
            "delay": "1",
            "descr": "",
            "dot1qEtherType": "0x8100",
            "duplex": "auto",
            "id": "eth1/1",
            "inhBw": "4294967295",
            "layer": "Layer2",
            "linkDebounce": "100",
            "linkDebounceLinkUp": "0",
            "linkLog": "default",
            "linkTransmitReset": "enable",
            "mdix": "auto",
            "medium": "broadcast",
            "mode": "access",
            "mtu": "1500",
            "name": "",
            "nativeVlan": "vlan-1",
            "persistentOnReload": "true",
            "portT": "leaf",
            "routerMac": "not-applicable",
            "snmpTrapSt": "enable",
            "spanMode": "not-a-span-dest",
            "speed": "auto",
            "speedGroup": "auto",
            "trunkLog": "default",
            "trunkVlans": "1-4094",
            "usage": "discovery",
            "userCfgdFlags": "",
            "voicePortCos": "none",
            "voicePortTrust": "disable",
            "voiceVlanId": "none",
            "voiceVlanType": "none"
        }
        self.Internal_Properties = {
            "childAction": "",
            "ethpmCfgFailedBmp": "",
            "ethpmCfgFailedTs": "00:00:00:00.000",
            "ethpmCfgState": "0",
            "modTs": "",
            "status": "",
            "switchingSt": "disabled",
            "voicePortCos": "none",
            "voicePortTrust": "disable",
            "voiceVlanId": "none",
            "voiceVlanType": "none"
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

    def local_payload_children(self, **kws):
        self.children = {
            "children": [kws]
        }

    def update_payload(self, pd={}):
        self.payload = {
            "l1PhysIf": {
            }
        }
        self.local_payload_att()
        self.payload["l1PhysIf"].update(self.att)
        return super().update_payload(self.payload)



a = l1PhysIf(id="eth1/1", mode="trunk", trunkVlans="10-20")
json.dumps(a.update_payload())


