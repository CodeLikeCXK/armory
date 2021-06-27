from arm.logicnode.arm_nodes import *

class GetLocationNode(ArmLogicTreeNode):
    """Get the location of the given object in world coordinates.
    
    @input Parent Relative: If enabled, transforms the world coordinates into object parent local coordinates

    @seeNode Set Object Location
    @seeNode World Vector to Local Space
    @seeNode Vector to Object Orientation
    """
    bl_idname = 'LNGetLocationNode'
    bl_label = 'Get Object Location'
    arm_section = 'location'
    arm_version = 1

    def init(self, context):
        super(GetLocationNode, self).init(context)
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_input('NodeSocketBool', 'Parent Relative')

        self.add_output('NodeSocketVector', 'Location')
