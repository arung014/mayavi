# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.socket import Socket


class ServerSocket(Socket):
    """
    ServerSocket - Encapsulate a socket that accepts connections.
    
    Superclass: Socket
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkServerSocket, obj, update, **traits)
    
    def _get_server_port(self):
        return self._vtk_obj.GetServerPort()
    server_port = traits.Property(_get_server_port, help=\
        """
        Returns the port on which the server is running.
        """
    )

    def create_server(self, *args):
        """
        V.create_server(int) -> int
        C++: int CreateServer(int port)
        Creates a server socket at a given port and binds to it. Returns
        -1 on error. 0 on success.
        """
        ret = self._wrap_call(self._vtk_obj.CreateServer, *args)
        return ret

    def wait_for_connection(self, *args):
        """
        V.wait_for_connection(int) -> ClientSocket
        C++: ClientSocket *WaitForConnection(unsigned long msec=0)
        Waits for a connection. When a connection is received a new
        ClientSocket object is created and returned. Returns NULL on
        timeout.
        """
        ret = self._wrap_call(self._vtk_obj.WaitForConnection, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ServerSocket, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ServerSocket properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ServerSocket properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ServerSocket properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
