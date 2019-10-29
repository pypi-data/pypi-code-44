# automatically generated by the FlatBuffers compiler, do not modify

# namespace: MNN

import flatbuffers

class Flatten(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFlatten(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Flatten()
        x.Init(buf, n + offset)
        return x

    # Flatten
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Flatten
    def Axis(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Flatten
    def EndAxis(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def FlattenStart(builder): builder.StartObject(2)
def FlattenAddAxis(builder, axis): builder.PrependInt32Slot(0, axis, 0)
def FlattenAddEndAxis(builder, endAxis): builder.PrependInt32Slot(1, endAxis, 0)
def FlattenEnd(builder): return builder.EndObject()
