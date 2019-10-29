# automatically generated by the FlatBuffers compiler, do not modify

# namespace: MNN

import flatbuffers

class MatMul(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMatMul(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MatMul()
        x.Init(buf, n + offset)
        return x

    # MatMul
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MatMul
    def T(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MatMul
    def TransposeA(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # MatMul
    def TransposeB(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # MatMul
    def Weight(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # MatMul
    def WeightAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # MatMul
    def WeightLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MatMul
    def Bias(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # MatMul
    def BiasAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # MatMul
    def BiasLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def MatMulStart(builder): builder.StartObject(5)
def MatMulAddT(builder, T): builder.PrependInt32Slot(0, T, 0)
def MatMulAddTransposeA(builder, transposeA): builder.PrependBoolSlot(1, transposeA, 0)
def MatMulAddTransposeB(builder, transposeB): builder.PrependBoolSlot(2, transposeB, 0)
def MatMulAddWeight(builder, weight): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(weight), 0)
def MatMulStartWeightVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MatMulAddBias(builder, bias): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(bias), 0)
def MatMulStartBiasVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MatMulEnd(builder): return builder.EndObject()
