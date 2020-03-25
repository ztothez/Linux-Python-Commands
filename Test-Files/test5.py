from sysdmanager import SystemdManager

manager = SystemdManager()
if not manager.is_active("bluetooth.service"):
    manager.status_unit("bluetooth.service")




































##import dbus


##service = 'networking'
##
##bus = dbus.SystemBus()
##systemd = bus.get_object(
##'org.freedesktop.systemd1.',
##'/org/freedesktop/systemd1'
##)
##manager = dbus.Interface(
##systemd,
##'org.freedesktop.systemd1.Manager'
##)
##
##service_unit = service if service.endswith('.service') else manager.GetUnit('{0}.service'.format(service))
##print("servers_unit",service_unit)
##service_proxy = bus.get_object('org.freedesktop.systemd1', str(service_unit))
##print("service_proxy",service_proxy)
##service_properties = dbus.Interface(service_proxy, dbus_interface='org.freedesktop.DBus.Properties')
##print("service_proreties",service_properties)
##service_load_state = service_properties.Get('org.freedesktop.systemd1.Unit', 'LoadState')
##print("service_load",service_load_state)
##service_active_state = service_properties.Get('org.freedesktop.systemd1.Unit', 'ActiveState')
##print("service_active",service_active_state)
####result = service.Get('org.freedesktop.systemd1.Service', result_prop,
####dbus_interface='org.freedesktop.DBus.Properties')
##
##if service_load_state == 'loaded' and service_active_state == 'active':
##print("Service Running")
##
##else:
##print("Service is not running")


#{'log':{'rivi1', 'rivi2'}}

##    result_prop = 'Result'
##    result = myservice_proxy.Get('org.freedesktop.systemd1.Service',
##                                 result_prop,
##                                 dbus_interface='org.freedesktop.DBus.Properties')
##    print(result)
