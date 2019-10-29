# automatically generated by the FlatBuffers compiler, do not modify

# namespace: MNN

import flatbuffers

class Relu(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRelu(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Relu()
        x.Init(buf, n + offset)
        return x

    # Relu
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Relu
    def Slope(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def ReluStart(builder): builder.StartObject(1)
def ReluAddSlope(builder, slope): builder.PrependFloat32Slot(0, slope, 0.0)
def ReluEnd(builder): return builder.EndObject()
