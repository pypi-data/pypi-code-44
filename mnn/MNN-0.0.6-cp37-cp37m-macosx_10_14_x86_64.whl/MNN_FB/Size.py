# automatically generated by the FlatBuffers compiler, do not modify

# namespace: MNN

import flatbuffers

class Size(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSize(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Size()
        x.Init(buf, n + offset)
        return x

    # Size
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Size
    def OutputDataType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def SizeStart(builder): builder.StartObject(1)
def SizeAddOutputDataType(builder, outputDataType): builder.PrependInt32Slot(0, outputDataType, 0)
def SizeEnd(builder): return builder.EndObject()
