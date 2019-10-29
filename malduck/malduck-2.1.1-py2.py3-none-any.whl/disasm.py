# Copyright (C) 2018 Jurriaan Bremer.
# This file is part of Roach - https://github.com/jbremer/roach.
# See the file 'docs/LICENSE.txt' for copying permission.

import collections
from .py2compat import is_string

Memory = collections.namedtuple(
    "Memory", ("size", "base", "scale", "index", "disp")
)


class Operand(object):
    """
    Operand object for single :class:`Instruction`
    """
    # These are initialized the first time disasm() is called, see also below.
    _x86_op_imm = None
    _x86_op_reg = None
    _x86_op_mem = None
    regs = {}

    sizes = {
        1: "byte", 2: "word", 4: "dword", 8: "qword",
    }

    def __init__(self, op, x64):
        self.op = op
        self.x64 = x64

    @property
    def is_imm(self):
        """Is it immediate operand?"""
        return self.op.type == Operand._x86_op_imm

    @property
    def is_reg(self):
        """Is it register operand?"""
        return self.op.type == Operand._x86_op_reg

    @property
    def is_mem(self):
        """Is it memory operand?"""
        return self.op.type == Operand._x86_op_mem

    @property
    def value(self):
        """
        Returns operand value or displacement value for memory operands

        :rtype: str or int
        """
        if self.is_imm:
            return self.op.value.imm
        if self.is_mem:
            return self.op.value.mem.disp
        if self.is_reg:
            return self.regs[self.op.reg]

    @property
    def reg(self):
        """
        Returns register used by operand.

        For memory operands, returns base register or index register if base is not used.
        For immediate operands or displacement-only memory operands returns None.

        :rtype: str
        """
        if self.is_mem:
            reg = self.op.value.mem.base or self.op.value.mem.index
            if reg:
                return self.regs[reg]
        if self.is_reg:
            return self.regs[self.op.reg]

    @property
    def mem(self):
        """
        Returns :class:`Memory` object for memory operands
        """
        if not self.is_mem:
            return
        mem = self.op.value.mem
        if mem.base:
            base = self.regs[mem.base]
        else:
            base = None
        if mem.index:
            index, scale = self.regs[mem.index], mem.scale
        else:
            index, scale = None, None
        return Memory(self.sizes[self.op.size], base, scale, index, mem.disp)

    def __eq__(self, other):
        if isinstance(other, Operand):
            return self.op.type == other.op.type and self.value == other.value
        if self.is_imm:
            return self.value == other
        if is_string(other):
            other = other,
        if self.is_reg and self.reg in other:
            return True
        if self.is_mem and self.reg in other:
            return True
        return False

    def __str__(self):
        if self.is_imm:
            if self.x64:
                return "0x%016x" % (self.value % 2**64)
            else:
                return "0x%08x" % (self.value % 2**32)
        if self.is_reg:
            return self.reg
        if self.is_mem:
            s, m = [], self.mem
            if m.base:
                s.append(m.base)
            if m.index:
                s.append("%d*%s" % (m.scale, m.index))
            if m.disp:
                s.append("0x%08x" % (m.disp % 2 ** 32))
            return "%s [%s]" % (m.size, "+".join(s))


class Instruction(object):
    """
    Represents single instruction in :class:`Disassemble`

    short: insn

    Properties correspond to the following elements of instruction:

    .. code-block:: python

        00400000  imul    ecx,   edx,   0
        [addr]    [mnem]  [op1], [op2], [op3]

    Usage example:

    .. code-block:: python

        def move_command_new(self, p, hit, *args):
            for c in p.disasmv(hit, 0x1000):
                if c.mnem == 'mov' and c.op1.value == 0x14:
                    return c.op2.value

    .. seealso::

       :py:meth:`malduck.procmem.ProcessMemory.disasmv`
    """
    def __init__(self, mnem=None, op1=None, op2=None, op3=None, addr=None, x64=False):
        self.insn = None
        self.mnem = mnem
        self.operands = op1, op2, op3
        self._addr = addr
        self.x64 = x64

    def parse(self, insn):
        self.insn = insn
        self.mnem = insn.mnemonic

        operands = []
        for op in insn.operands + [None, None, None]:
            operands.append(Operand(op, self.x64) if op else None)
        self.operands = operands[0], operands[1], operands[2]

    @staticmethod
    def from_capstone(insn, x64=False):
        ret = Instruction()
        ret.x64 = x64
        ret.parse(insn)
        return ret

    @property
    def op1(self):
        """First operand"""
        return self.operands[0]

    @property
    def op2(self):
        """Second operand"""
        return self.operands[1]

    @property
    def op3(self):
        """Third operand"""
        return self.operands[2]

    @property
    def addr(self):
        """Instruction address"""
        return self._addr or self.insn.address

    def __eq__(self, other):
        if not isinstance(other, Instruction):
            return False
        if self.mnem != other.mnem or self.addr != other.addr:
            return False
        if self.operands == other.operands:
            return True
        return False

    def __str__(self):
        operands = []
        if self.op1 is not None:
            operands.append(str(self.op1))
        if self.op2 is not None:
            operands.append(str(self.op2))
        if self.op3 is not None:
            operands.append(str(self.op3))
        if operands:
            return "%s %s" % (self.mnem, ", ".join(operands))
        return self.mnem


class Disassemble(object):
    def disassemble(self, data, addr, x64=False):
        """
        Disassembles data from specific address

        short: disasm

        :param data: Block of data to disasseble
        :type data: bytes
        :param addr: Virtual address of data
        :type addr: int
        :param x64: Disassemble in x86-64 mode?
        :type x64: bool (default=False)
        :return: Returns list of instructions
        :rtype: List[:class:`Instruction`]
        """
        import capstone

        cs = capstone.Cs(capstone.CS_ARCH_X86,
                         capstone.CS_MODE_64 if x64 else capstone.CS_MODE_32)
        cs.detail = True
        ret = []
        for insn in cs.disasm(data, addr):
            ret.append(Instruction.from_capstone(insn, x64=x64))
        return ret

    def init_once(self, *args, **kwargs):
        import capstone.x86

        Operand._x86_op_imm = capstone.x86.X86_OP_IMM
        Operand._x86_op_reg = capstone.x86.X86_OP_REG
        Operand._x86_op_mem = capstone.x86.X86_OP_MEM

        # Index the available x86 registers.
        for _ in dir(capstone.x86):
            if not _.startswith("X86_REG_"):
                continue
            Operand.regs[getattr(capstone.x86, _)] = _.split("_")[2].lower()

        self.__call__ = self.disassemble
        return self.__call__(*args, **kwargs)

    __call__ = init_once


disasm = Disassemble()
