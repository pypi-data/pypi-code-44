# automatically generated by the FlatBuffers compiler, do not modify

# namespace: MNN

import flatbuffers

class Permute(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPermute(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Permute()
        x.Init(buf, n + offset)
        return x

    # Permute
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Permute
    def Dims(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # Permute
    def DimsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # Permute
    def DimsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def PermuteStart(builder): builder.StartObject(1)
def PermuteAddDims(builder, dims): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(dims), 0)
def PermuteStartDimsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def PermuteEnd(builder): return builder.EndObject()
