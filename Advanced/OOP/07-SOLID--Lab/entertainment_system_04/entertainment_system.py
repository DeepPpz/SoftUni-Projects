class HDMICable:
    def connect_to_device_via_hdmi_cable(self, device):
        return f"Connected to {device} via HDMI"


class RCACable:
    def connect_to_device_via_rca_cable(self, device):
        return f"Connected to {device} via RCA"


class EthernetCable:
    def connect_to_device_via_ethernet_cable(self, device):
        return f"Connected to {device} via Ethernet"


class PowerOutlet:
    def connect_device_to_power_outlet(self, device):
        return f"Connected to electricty via Power Outlet"


class Television(RCACable, EthernetCable, PowerOutlet):
    def __init__(self):
        self.dvd_connected = False
        self.router_connected = False
        self.electricity_connected = False
    
    def connect_to_dvd(self, dvd_player):
        self.dvd_connected = True
        return self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_router(self, router):
        self.router_connected = True
        return self.connect_to_device_via_ethernet_cable(router)
    
    def plug_in_power(self):
        self.electricity_connected = True
        return self.connect_device_to_power_outlet(self)


class DVDPlayer(HDMICable, PowerOutlet):
    def __init__(self):
        self.television_connected = False
        self.power_connected = False
    
    def connect_to_tv(self, television):
        self.television_connected = True
        return self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.electricity_connected = True
        return self.connect_device_to_power_outlet(self)


class GameConsole(HDMICable, EthernetCable, PowerOutlet):
    def __init__(self):
        self.television_connected = False
        self.router_connected = False
        self.electricity_connected = False
    
    def connect_to_tv(self, television):
        self.television_connected = True
        return self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.router_connected = True
        return self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.electricity_connected = True
        return self.connect_device_to_power_outlet(self)


class Router(PowerOutlet):
    def __init__(self):
        self.electricity_connected = False

    def plug_in_power(self):
        self.electricity_connected = True
        return self.connect_device_to_power_outlet(self)
