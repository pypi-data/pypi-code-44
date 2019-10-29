# -*- coding: utf-8 -*-
import functools
import random
import string
import os

try:
    text_type = unicode
except NameError:
    text_type = str

HEXLIFY_CHARS = "0123456789abcdefABCDEF"
URLSAFEB64_CHARS = "-0123456789=ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz\r\n"
BASE64_CHARS = "+/0123456789=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\r\n"

default_encodings = ["utf8", "gb18030"]


def random_string(length, choices=string.ascii_letters):
    text = ""
    for _ in range(0, length):
        text += random.choice(choices)
    return text

def char_force_to_int(value):
    if isinstance(value, int):
        return value
    return ord(value)

def force_text(value, encoding=None):
    if isinstance(value, text_type):
        return value
    if not encoding:
        encodings = default_encodings
    elif isinstance(encoding, (set, list, tuple)):
        encodings = encoding
    else:
        encodings = [encoding]
    for encoding in encodings:
        try:
            print(value, encoding)
            return value.decode(encoding)
        except UnicodeDecodeError:
            pass
    raise UnicodeDecodeError()

def wholestrip(text):
    """Remove all white spaces in text. White spaces are ' \t\n\r\x0b\x0c\u3000'.
    """
    for space in string.whitespace + u'\u3000':
        text = text.replace(space, "")
    return text


def split(text, seps, strip=False):
    """seps is a list of string, all sep in the seps are treated as delimiter.
    """
    if not isinstance(seps, (list, set, tuple)):
        seps = [seps]
    results = [text]
    for sep in seps:
        row = []
        for value in results:
            row += value.split(sep)
        results = row
    if strip:
        row = []
        for value in results:
            row.append(value.strip())
        results = row
    return results


def str_composed_by(text, choices):
    """Test if text is composed by chars in the choices.
    """
    for char in text:
        if not char in choices:
            return False
    return True

is_str_composed_by_the_choices = str_composed_by


def is_hex_digits(text):
    """Test if all chars in text is hex digits.
    """
    if not text:
        return False
    return str_composed_by(text, HEXLIFY_CHARS)

def join_lines(text):
    """Join multi-lines into single line.
    """
    return "".join(text.splitlines())


def is_urlsafeb64_decodable(text):
    """Test if the text can be decoded by urlsafeb64 method.
    """
    text = wholestrip(text)
    if not text:
        return False
    if len(text) % 4 != 0:
        return False
    return str_composed_by(join_lines(text), URLSAFEB64_CHARS)


def is_base64_decodable(text):
    """Test  if the text can be decoded by base64 method.
    """
    text = wholestrip(text)
    if not text:
        return False
    if len(text) % 4 != 0:
        return False
    return str_composed_by(join_lines(text), BASE64_CHARS)


def is_unhexlifiable(text):
    """Test if the text can be decoded by unhexlify method.
    """
    text = wholestrip(text)
    if not text:
        return False
    if len(text) % 2 != 0:
        return False
    return str_composed_by(text, HEXLIFY_CHARS)


def text_display_length(text, unicode_display_length=2, encoding=None):
    """Get text display length.
    """
    text = force_text(text, encoding)
    length = 0
    for c in text:
        if ord(c) <= 128:
            length += 1
        else:
            length += unicode_display_length
    return length

def text_display_shorten(text, max_length, unicode_display_length=2, suffix="...", encoding=None):
    """Shorten text to fix the max display length.
    """
    text = force_text(text, encoding)
    if max_length < len(suffix):
        max_length = len(suffix)
    tlen = text_display_length(text, unicode_display_length=unicode_display_length)
    if tlen <= max_length:
        return text
    result = ""
    tlen = 0
    max_length -= len(suffix)
    for c in text:
        if ord(c) <= 128:
            tlen += 1
        else:
            tlen += unicode_display_length
        if tlen < max_length:
            result += c
        elif tlen == max_length:
            result += c
            break
        else:
            break
    result += suffix
    return result
