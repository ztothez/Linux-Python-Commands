import dbus
def get_access_point_all_info(self, ap_path):

    bus = dbus.SystemBus()
    obj = bus.get_object('org.freedesktop.NetworkManager', ap_path)

    iface = dbus.Interface(obj, dbus_interface='org.freedesktop.DBus.Properties')
    print(iface)
    m = iface.get_dbus_method("GetAll", dbus_interface=None)
    print(m)

    # getting all ppoperties like Ssid, Strength, HwAddress etc.
    props = m("org.freedesktop.NetworkManager.AccessPoint")
    print(props)
