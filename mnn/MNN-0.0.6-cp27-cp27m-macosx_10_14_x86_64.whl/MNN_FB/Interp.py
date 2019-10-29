# automatically generated by the FlatBuffers compiler, do not modify

# namespace: MNN

import flatbuffers

class Interp(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsInterp(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Interp()
        x.Init(buf, n + offset)
        return x

    # Interp
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Interp
    def WidthScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Interp
    def HeightScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Interp
    def OutputWidth(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Interp
    def OutputHeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Interp
    def ResizeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Interp
    def AlignCorners(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def InterpStart(builder): builder.StartObject(6)
def InterpAddWidthScale(builder, widthScale): builder.PrependFloat32Slot(0, widthScale, 0.0)
def InterpAddHeightScale(builder, heightScale): builder.PrependFloat32Slot(1, heightScale, 0.0)
def InterpAddOutputWidth(builder, outputWidth): builder.PrependInt32Slot(2, outputWidth, 0)
def InterpAddOutputHeight(builder, outputHeight): builder.PrependInt32Slot(3, outputHeight, 0)
def InterpAddResizeType(builder, resizeType): builder.PrependInt32Slot(4, resizeType, 0)
def InterpAddAlignCorners(builder, alignCorners): builder.PrependBoolSlot(5, alignCorners, 0)
def InterpEnd(builder): return builder.EndObject()
