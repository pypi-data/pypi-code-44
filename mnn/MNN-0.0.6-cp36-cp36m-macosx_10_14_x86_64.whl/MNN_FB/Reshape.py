# automatically generated by the FlatBuffers compiler, do not modify

# namespace: MNN

import flatbuffers

class Reshape(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsReshape(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Reshape()
        x.Init(buf, n + offset)
        return x

    # Reshape
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Reshape
    def Dims(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # Reshape
    def DimsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # Reshape
    def DimsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Reshape
    def DimType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def ReshapeStart(builder): builder.StartObject(2)
def ReshapeAddDims(builder, dims): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(dims), 0)
def ReshapeStartDimsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ReshapeAddDimType(builder, dimType): builder.PrependInt8Slot(1, dimType, 0)
def ReshapeEnd(builder): return builder.EndObject()
