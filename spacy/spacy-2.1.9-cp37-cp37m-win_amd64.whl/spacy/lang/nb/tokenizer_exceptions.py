# encoding: utf8
from __future__ import unicode_literals

from ...symbols import ORTH, LEMMA


_exc = {}


for exc_data in [
    {ORTH: "jan.", LEMMA: "januar"},
    {ORTH: "feb.", LEMMA: "februar"},
    {ORTH: "mar.", LEMMA: "mars"},
    {ORTH: "apr.", LEMMA: "april"},
    {ORTH: "jun.", LEMMA: "juni"},
    {ORTH: "jul.", LEMMA: "juli"},
    {ORTH: "aug.", LEMMA: "august"},
    {ORTH: "sep.", LEMMA: "september"},
    {ORTH: "okt.", LEMMA: "oktober"},
    {ORTH: "nov.", LEMMA: "november"},
    {ORTH: "des.", LEMMA: "desember"},
]:
    _exc[exc_data[ORTH]] = [exc_data]


for orth in [
    "adm.dir.",
    "a.m.",
    "andelsnr",
    "Aq.",
    "b.c.",
    "bl.a.",
    "bla.",
    "bm.",
    "bnr.",
    "bto.",
    "ca.",
    "cand.mag.",
    "c.c.",
    "co.",
    "d.d.",
    "dept.",
    "d.m.",
    "dr.philos.",
    "dvs.",
    "d.y.",
    "E. coli",
    "eg.",
    "ekskl.",
    "e.Kr.",
    "el.",
    "e.l.",
    "et.",
    "etc.",
    "etg.",
    "ev.",
    "evt.",
    "f.",
    "f.eks.",
    "fhv.",
    "fk.",
    "f.Kr.",
    "f.o.m.",
    "foreg.",
    "fork.",
    "fv.",
    "fvt.",
    "g.",
    "gt.",
    "gl.",
    "gno.",
    "gnr.",
    "grl.",
    "hhv.",
    "hoh.",
    "hr.",
    "h.r.adv.",
    "ifb.",
    "ifm.",
    "iht.",
    "inkl.",
    "istf.",
    "jf.",
    "jr.",
    "jun.",
    "kfr.",
    "kgl.res.",
    "kl.",
    "komm.",
    "kr.",
    "kst.",
    "lø.",
    "ma.",
    "mag.art.",
    "m.a.o.",
    "md.",
    "mfl.",
    "mill.",
    "min.",
    "m.m.",
    "mnd.",
    "moh.",
    "Mr.",
    "muh.",
    "mv.",
    "mva.",
    "ndf.",
    "no.",
    "nov.",
    "nr.",
    "nto.",
    "nyno.",
    "n.å.",
    "o.a.",
    "off.",
    "ofl.",
    "okt.",
    "o.l.",
    "on.",
    "op.",
    "org."
    "osv.",
    "ovf.",
    "p.",
    "p.a.",
    "Pb.",
    "pga.",
    "ph.d.",
    "pkt.",
    "p.m.",
    "pr.",
    "pst.",
    "p.t.",
    "red.anm.",
    "ref.",
    "res.",
    "res.kap.",
    "resp.",
    "rv.",
    "s.",
    "s.d.",
    "sen.",
    "sep.",
    "siviling.",
    "sms.",
    "snr.",
    "spm.",
    "sr.",
    "sst.",
    "st.",
    "stip.",
    "stk.",
    "st.meld.",
    "st.prp.",
    "stud.",
    "s.u.",
    "sv.",
    "sø.",
    "s.å.",
    "såk.",
    "temp.",
    "ti.",
    "tils.",
    "tilsv.",
    "tl;dr",
    "tlf.",
    "to.",
    "t.o.m.",
    "ult.",
    "utg.",
    "v.",
    "vedk.",
    "vedr.",
    "vg.",
    "vgs.",
    "vha.",
    "vit.ass.",
    "vn.",
    "vol.",
    "vs.",
    "vsa.",
    "årg.",
    "årh.",
]:
    _exc[orth] = [{ORTH: orth}]


TOKENIZER_EXCEPTIONS = _exc
