# -*- coding: utf-8 -*-

import functools

from django import forms

from .lomake import yhdista_lomakkeet
from .sarja import lisaa_lomakesarja


def nido(*args, **kwargs):
  if len(args) > 2:
    return functools.reduce(functools.partial(nido, **kwargs), args)

  elif len(args) == 1:
    def koriste(lomake_a):
      return nido(lomake_a, *args, **kwargs)
    return koriste

  lomake_a, lomake_b = args
  if not issubclass(lomake_a, forms.ModelForm):
    raise ValueError(
      f'Liitettävien lomakkeiden tulee olla tyyppiä `forms.ModelForm`,'
      f' ei {type(lomake_a)!r}'
    )
  if not issubclass(lomake_b, forms.ModelForm):
    raise ValueError(
      f'Liitettävien lomakkeiden tulee olla tyyppiä `forms.ModelForm`,'
      f' ei {type(lomake_b)!r}'
    )

  if 'avain_a' in kwargs:
    avain_a = kwargs.pop('avain_a')
  else:
    avain_a, = (
      f.name for f in lomake_a.Meta.model._meta.get_fields()
      if f.is_relation and f.related_model == lomake_b.Meta.model
    )
  if avain_a is not None:
    kwargs['avain_a'] = avain_a

  if 'avain_b' in kwargs:
    avain_b = kwargs.pop('avain_b')
  else:
    avain_b, = (
      f.name for f in lomake_b.Meta.model._meta.get_fields()
      if f.is_relation and f.related_model == lomake_a.Meta.model
    )
  if avain_b is not None:
    kwargs['avain_b'] = avain_b

  useita = kwargs.pop('useita', None)
  if useita is None:
    if avain_a is not None:
      viittaus = lomake_a.Meta.model._meta.get_field(avain_a)
      useita = viittaus.one_to_many or viittaus.many_to_many
    elif avain_b is not None:
      viittaus = lomake_b.Meta.model._meta.get_field(avain_b)
      useita = viittaus.many_to_one or viittaus.many_to_many
    else:
      raise ValueError(
        'Mallien välisen viittaussuhteen lukuisuutta ei voitu päätellä.'
        ' Joko `avain_a` tai `avain_b` on oltava `!= None`.'
      )
    # if useita is None

  if useita:
    from django.contrib.contenttypes.fields import GenericForeignKey
    epasuora = isinstance(
      lomake_b.Meta.model._meta.get_field(avain_b),
      GenericForeignKey,
    )
    kwargs['epasuora'] = epasuora

  return (lisaa_lomakesarja if useita else yhdista_lomakkeet)(*args, **kwargs)
  # def nido
