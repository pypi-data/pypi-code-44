# automatically generated by the FlatBuffers compiler, do not modify

# namespace: MNN

import flatbuffers

class SliceTf(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSliceTf(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SliceTf()
        x.Init(buf, n + offset)
        return x

    # SliceTf
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SliceTf
    def T(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def SliceTfStart(builder): builder.StartObject(1)
def SliceTfAddT(builder, T): builder.PrependInt32Slot(0, T, 0)
def SliceTfEnd(builder): return builder.EndObject()
