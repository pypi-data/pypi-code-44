# automatically generated by the FlatBuffers compiler, do not modify

# namespace: MNN

import flatbuffers

class AsString(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAsString(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AsString()
        x.Init(buf, n + offset)
        return x

    # AsString
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AsString
    def T(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # AsString
    def Precision(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # AsString
    def Scientific(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # AsString
    def Shortest(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # AsString
    def Width(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # AsString
    def FillString(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def AsStringStart(builder): builder.StartObject(6)
def AsStringAddT(builder, T): builder.PrependInt32Slot(0, T, 0)
def AsStringAddPrecision(builder, precision): builder.PrependInt32Slot(1, precision, 0)
def AsStringAddScientific(builder, scientific): builder.PrependBoolSlot(2, scientific, 0)
def AsStringAddShortest(builder, shortest): builder.PrependBoolSlot(3, shortest, 0)
def AsStringAddWidth(builder, width): builder.PrependInt32Slot(4, width, 0)
def AsStringAddFillString(builder, fillString): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(fillString), 0)
def AsStringEnd(builder): return builder.EndObject()
