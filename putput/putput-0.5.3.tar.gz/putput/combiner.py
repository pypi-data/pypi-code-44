from functools import reduce
from itertools import repeat
from typing import Callable
from typing import Iterable
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Tuple

from putput.joiner import ComboOptions
from putput.joiner import join_combo


def combine(utterance_combo: Sequence[Sequence[str]],
            tokens: Sequence[str],
            groups: Sequence[Tuple[str, int]],
            *,
            token_handler_map: Optional[Mapping[str, Callable[[str, str], str]]] = None,
            group_handler_map: Optional[Mapping[str, Callable[[str, Sequence[str]], str]]] = None,
            combo_options: Optional[ComboOptions] = None
            ) -> Tuple[int, Iterable[Tuple[str, Sequence[str], Sequence[str]]]]:
    """Generates an utterance, handled tokens, and handled groups.

    Args:
        utterance_combo: An utterance_combo from pipeline.expander.expand.

        tokens: Tokens that have yet to be handled from pipeline.expander.expand.

        groups: Groups that have yet to be handled from pipeline.expander.expand.

        token_handler_map: A mapping between a token and a function with args
            (token, phrase generated by token) that returns a handled token. If 'DEFAULT'
            is specified as the token, the handler will apply to all tokens not otherwise
            specified in the mapping.

        combo_options: Options for randomly sampling the combination of 'utterance_combo'.

    Returns:
        The length of the Iterable, and the Iterable consisting of an utterance
        and handled tokens.

    Examples:
        >>> def _iob_token_handler(token: str, phrase: str) -> str:
        ...     tokens = ['{}-{}'.format('B' if i == 0 else 'I', token)
        ...               for i, _ in enumerate(phrase.replace(" '", "'").split())]
        ...     return ' '.join(tokens)
        >>> def _just_groups(group_name: str, _: Sequence[str]) -> str:
        ...     return '[{}]'.format(group_name)
        >>> token_handler_map = {'DEFAULT': _iob_token_handler}
        >>> group_handler_map = {'DEFAULT': _just_groups}
        >>> combo_options = ComboOptions(max_sample_size=2, with_replacement=False)
        >>> utterance_combo = (('can she get', 'may she get'), ('fries',))
        >>> tokens = ('ADD', 'ITEM')
        >>> groups = (('ADD_ITEM', 2),)
        >>> sample_size, generator = combine(utterance_combo,
        ...                                  tokens,
        ...                                  groups,
        ...                                  token_handler_map=token_handler_map,
        ...                                  group_handler_map=group_handler_map,
        ...                                  combo_options=combo_options)
        >>> sample_size
        2
        >>> for utterance, handled_tokens, handled_groups in generator:
        ...     print(utterance)
        ...     print(handled_tokens)
        ...     print(handled_groups)
        can she get fries
        ('B-ADD I-ADD I-ADD', 'B-ITEM')
        ('[ADD_ITEM]',)
        may she get fries
        ('B-ADD I-ADD I-ADD', 'B-ITEM')
        ('[ADD_ITEM]',)
    """
    sample_size = reduce(lambda x, y: x * y, (len(item) for item in utterance_combo))
    if combo_options:
        sample_size = combo_options.max_sample_size

    def _combine() -> Iterable[Tuple[str, Sequence[str], Sequence[str]]]:
        for utterance_components in join_combo(utterance_combo, combo_options=combo_options):
            handled_tokens = _compute_handled_tokens(utterance_components, tokens, token_handler_map=token_handler_map)
            handled_groups = _compute_handled_groups(groups, handled_tokens, group_handler_map)
            yield ' '.join(utterance_components), handled_tokens, handled_groups
    return sample_size, _combine()

def _compute_handled_tokens(utterance_components: Sequence[str],
                            tokens: Sequence[str],
                            *,
                            token_handler_map: Optional[Mapping[str, Callable[[str, str], str]]]
                            ) -> Sequence[str]:
    return tuple(map(lambda utc, token, th_map: _get_token_handler(token, token_handler_map=th_map)(token, utc),
                     utterance_components, tokens, repeat(token_handler_map)))

def _get_token_handler(token: str,
                       *,
                       token_handler_map: Optional[Mapping[str, Callable[[str, str], str]]] = None
                       ) -> Callable[[str, str], str]:
    default_token_handler = lambda token, phrase: '[{}({})]'.format(token, phrase)
    if token_handler_map:
        return token_handler_map.get(token) or token_handler_map.get('DEFAULT') or default_token_handler
    return default_token_handler

def _compute_handled_groups(groups: Sequence[Tuple[str, int]],
                            handled_tokens: Sequence[str],
                            group_handler_map: Optional[Mapping[str, Callable[[str, Sequence[str]], str]]]
                            ) -> Sequence[str]:
    start_index = 0
    handled_groups = []
    for group in groups:
        group_name, end_index = group
        group_handler = _get_group_handler(group_name, group_handler_map)
        handled_group = group_handler(group_name, handled_tokens[start_index: start_index + end_index])
        handled_groups.append(handled_group)
        start_index += end_index
    return tuple(handled_groups)

def _get_group_handler(group_name: str,
                       group_handler_map: Optional[Mapping[str, Callable[[str, Sequence[str]], str]]]
                       ) -> Callable[[str, Sequence[str]], str]:
    default_group_handler = lambda group_name, handled_tokens: '{{{}({})}}'.format(group_name,
                                                                                   ' '.join(handled_tokens))
    if group_handler_map:
        return (group_handler_map.get(group_name) or
                group_handler_map.get('DEFAULT') or
                default_group_handler)
    return default_group_handler
