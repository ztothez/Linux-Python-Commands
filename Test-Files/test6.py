import dbus

def is_service_running(service):
    service_running = False
    bus = dbus.SystemBus()
    systemd = bus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
    manager = dbus.getInterface(systemd, dbus_interface='org.freedesktop.systemd1.Manager')
    try:
        service_unit = service if service.endswith('.service') else manager.GetUnit('{0}.service'.format(service))
        service_proxy = bus.get_object('org.freedesktop.systemd1', str(service_unit))
        service_properties = Interface(service_proxy, dbus_interface='org.freedesktop.DBus.Properties')
        service_load_state = service_properties.Get('org.freedesktop.systemd1.Unit', 'LoadState')
        service_active_state = service_properties.Get('org.freedesktop.systemd1.Unit', 'ActiveState')
        if service_load_state == 'loaded' and service_active_state == 'active':
            service_running = True
    except DBusException:
        pass

    return service_running 
is_service_running("network-manager.service")
