"""The MayaVi view in Envisage.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import join

# Enthought library imports.
from enthought.traits.api import Instance, HasTraits, Any
from enthought.traits.ui.api import (Group, Item, TreeEditor, TreeNode,
        ObjectTreeNode, View, Handler, UIInfo)
from enthought.resource.resource_path import resource_path
from enthought.pyface.image_resource import ImageResource

# Local imports.
from enthought.mayavi.core.engine import Engine
from enthought.mayavi.core.base import Base
from enthought.mayavi.core.adder_node import AdderNode

class EngineViewHandler(Handler):
    """ A handler for the EngineView object. 
    """

    info = Instance(UIInfo)

    def init_info(self, info):
        """ Informs the handler what the UIInfo object for a View will be.
        Overridden here to save a reference to the info object.
        
        """
        self.info = info
        return

    def _on_dclick(self, object):
        """ Called when a node in the tree editor is double-clicked.
        """
        object.edit_traits(view=object.dialog_view(), 
                           parent=self.info.ui.control )

    def _on_select(self, object):
        """ Called when a node in the tree editor is selected.
        """
        if isinstance(object, AdderNode):
            self._on_dclick(object)
        else:
            self.info.object.engine._on_select(object)


##############################################################################
# EngineView class.
##############################################################################
class EngineView(HasTraits):
    """ A view displaying the engine's object tree. """

    # The MayaVi engine we are a view of.
    engine = Instance(Engine, allow_none=True)
   
    icon = ImageResource(join(resource_path(), 'images', 'mv2.ico'))

    # Nodes on the tree.
    nodes = Any

    ###########################################################################
    # `object` interface.
    ###########################################################################
    def __init__(self, **traits):
        super(EngineView, self).__init__(**traits)

                
    ###########################################################################
    # `HasTraits` interface.
    ###########################################################################
    def default_traits_view(self):
        """The default traits view of the Engine View.
        """
        
        tree_editor = TreeEditor(editable=False,
                                 hide_root=True,
                                 on_dclick='handler._on_dclick',
                                 on_select='handler._on_select',
                                 orientation='vertical',
                                 selected='object.engine.current_selection',
                                 nodes=self.nodes
                                 )


        view = View(Group(Item(name='engine',
                               id='engine',
                               editor=tree_editor,
                               resizable=True ),
                          show_labels=False,
                          show_border=False,
                          orientation='vertical'),
                    id='enthought.mayavi.engine',
                    help=False,
                    resizable=True,
                    undo=False,
                    revert=False,
                    ok=False,
                    cancel=False,
                    title='Mayavi pipeline',
                    icon=self.icon,
                    width=0.3,
                    height=0.3,
                    handler = EngineViewHandler)
        return view
    

    def _nodes_default(self):
        """ The default value of the cached nodes list.
        """
        # Now setup the view.
        nodes = [TreeNode(node_for=[Engine],
                          children='children_ui_list',
                          label='=Mayavi',
                          auto_open=False,
                          copy=False,
                          delete=False,
                          rename=False,
                          ),
                 ObjectTreeNode(node_for=[Base],
                                children='children',
                                label='name',
                                auto_open=True,
                                copy=True,
                                delete=True,
                                rename=True,
                                tooltip='=Right click for more options',
                                ),
                 TreeNode(node_for=[AdderNode],
                          children='',
                          label='label',
                          auto_open=True,
                          copy=False,
                          delete_me=False,
                          rename_me=False,
                          tooltip='tooltip',
                          icon_path=resource_path(),
                          icon_item='add.ico',
                          ),
                 
                 ]
        return nodes

  
    
### EOF ######################################################################