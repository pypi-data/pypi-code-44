import pickle

from revscoring.datasources.datasource import Datasource
from revscoring.datasources.meta import frequencies
from revscoring.dependencies import solve

old_tokens = Datasource("old_tokens")
new_tokens = Datasource("new_tokens")

old_ft = frequencies.table(old_tokens, name="old_ft")
new_ft = frequencies.table(new_tokens, name="new_ft")

delta = frequencies.delta(old_ft, new_ft, name="delta")
pos_delta = frequencies.positive(delta, name="pos_delta")
neg_delta = frequencies.negative(delta, name="neg_delta")
neg_abs_delta = frequencies.negative(
    delta, absolute=True, name="neg_abs_delta")

prop_delta = frequencies.prop_delta(old_ft, delta, name="prop_delta")


def test_table():
    cache = {new_tokens: ["a"] * 3 + ["b"] * 2 + ["c"] * 45}
    assert (solve(new_ft, cache=cache) ==
            {'a': 3, 'b': 2, 'c': 45})

    assert (pickle.loads(pickle.dumps(new_ft)) ==
            new_ft)


def test_delta():
    cache = {old_tokens: ["a"] * 3 + ["b"] * 2 + ["c"] * 45,
             new_tokens: ["a"] * 1 + ["b"] * 5 + ["d"] * 3}
    assert (solve(delta, cache=cache) ==
            {'a': -2, 'b': 3, 'c': -45, 'd': 3})

    assert (pickle.loads(pickle.dumps(delta)) ==
            delta)


def test_prop_delta():
    cache = {old_tokens: ["a"] * 3 + ["b"] * 2 + ["c"] * 45 + ["e"] * 2,
             new_tokens: ["a"] * 1 + ["b"] * 5 + ["d"] * 3 + ["e"] * 3}

    pd = solve(prop_delta, cache=cache)
    assert pd.keys() == {'a', 'b', 'c', 'd', 'e'}
    assert round(pd['a'], 2) == -0.67
    assert round(pd['b'], 2) == 1
    assert round(pd['c'], 2) == -1
    assert round(pd['d'], 2) == 3
    assert round(pd['e'], 2) == 0.33

    assert (pickle.loads(pickle.dumps(prop_delta)) ==
            prop_delta)


def test_positive():
    cache = {old_tokens: ["a"] * 3 + ["b"] * 2 + ["c"] * 45 + ["e"] * 2,
             new_tokens: ["a"] * 1 + ["b"] * 5 + ["d"] * 3 + ["e"] * 3}
    assert (solve(pos_delta, cache=cache) ==
            {'b': 3, 'd': 3, 'e': 1})


def test_negative():
    cache = {old_tokens: ["a"] * 3 + ["b"] * 2 + ["c"] * 45 + ["e"] * 2,
             new_tokens: ["a"] * 1 + ["b"] * 5 + ["d"] * 3 + ["e"] * 3}
    assert (solve(neg_delta, cache=cache) ==
            {'a': -2, 'c': -45})

    cache = {old_tokens: ["a"] * 3 + ["b"] * 2 + ["c"] * 45 + ["e"] * 2,
             new_tokens: ["a"] * 1 + ["b"] * 5 + ["d"] * 3 + ["e"] * 3}
    assert (solve(neg_abs_delta, cache=cache) ==
            {'a': 2, 'c': 45})
