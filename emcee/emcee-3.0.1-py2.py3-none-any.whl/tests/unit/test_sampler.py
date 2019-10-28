# -*- coding: utf-8 -*-

import pickle
from itertools import product

import numpy as np
import pytest

from emcee import EnsembleSampler, backends, moves

__all__ = ["test_shapes", "test_errors", "test_thin", "test_vectorize"]

all_backends = backends.get_test_backends()


def normal_log_prob(params):
    return -0.5 * np.sum(params ** 2)


@pytest.mark.parametrize(
    "backend, moves",
    product(
        all_backends,
        [
            None,
            moves.GaussianMove(0.5),
            [moves.StretchMove(), moves.GaussianMove(0.5)],
            [(moves.StretchMove(), 0.3), (moves.GaussianMove(0.5), 0.1)],
        ],
    ),
)
def test_shapes(backend, moves, nwalkers=32, ndim=3, nsteps=10, seed=1234):
    # Set up the random number generator.
    np.random.seed(seed)

    with backend() as be:
        # Initialize the ensemble, moves and sampler.
        coords = np.random.randn(nwalkers, ndim)
        sampler = EnsembleSampler(
            nwalkers, ndim, normal_log_prob, moves=moves, backend=be
        )

        # Run the sampler.
        sampler.run_mcmc(coords, nsteps)
        chain = sampler.get_chain()
        assert len(chain) == nsteps, "wrong number of steps"

        tau = sampler.get_autocorr_time(quiet=True)
        assert tau.shape == (ndim,)

        # Check the shapes.
        with pytest.warns(DeprecationWarning):
            assert sampler.chain.shape == (
                nwalkers,
                nsteps,
                ndim,
            ), "incorrect coordinate dimensions"
        with pytest.warns(DeprecationWarning):
            assert sampler.lnprobability.shape == (
                nwalkers,
                nsteps,
            ), "incorrect probability dimensions"
        assert sampler.get_chain().shape == (
            nsteps,
            nwalkers,
            ndim,
        ), "incorrect coordinate dimensions"
        assert sampler.get_log_prob().shape == (
            nsteps,
            nwalkers,
        ), "incorrect probability dimensions"

        assert sampler.acceptance_fraction.shape == (
            nwalkers,
        ), "incorrect acceptance fraction dimensions"

        # Check the shape of the flattened coords.
        assert sampler.get_chain(flat=True).shape == (
            nsteps * nwalkers,
            ndim,
        ), "incorrect coordinate dimensions"
        assert sampler.get_log_prob(flat=True).shape == (
            nsteps * nwalkers,
        ), "incorrect probability dimensions"


@pytest.mark.parametrize("backend", all_backends)
def test_errors(backend, nwalkers=32, ndim=3, nsteps=5, seed=1234):
    # Set up the random number generator.
    np.random.seed(seed)

    with backend() as be:
        # Initialize the ensemble, proposal, and sampler.
        coords = np.random.randn(nwalkers, ndim)
        sampler = EnsembleSampler(nwalkers, ndim, normal_log_prob, backend=be)

        # Test for not running.
        with pytest.raises(AttributeError):
            sampler.get_chain()
        with pytest.raises(AttributeError):
            sampler.get_log_prob()

        # What about not storing the chain.
        sampler.run_mcmc(coords, nsteps, store=False)
        with pytest.raises(AttributeError):
            sampler.get_chain()

        # Now what about if we try to continue using the sampler with an
        # ensemble of a different shape.
        sampler.run_mcmc(coords, nsteps, store=False)

        coords2 = np.random.randn(nwalkers, ndim + 1)
        with pytest.raises(ValueError):
            list(sampler.run_mcmc(coords2, nsteps))

        # Ensure that a warning is logged if the inital coords don't allow
        # the chain to explore all of parameter space, and that one is not
        # if we explicitly disable it, or the initial coords can.
        with pytest.warns(RuntimeWarning) as recorded_warnings:
            sampler.run_mcmc(np.ones((nwalkers, ndim)), nsteps)
            assert len(recorded_warnings) == 1
        with pytest.warns(None) as recorded_warnings:
            sampler.run_mcmc(
                np.ones((nwalkers, ndim)),
                nsteps,
                skip_initial_state_check=True,
            )
            sampler.run_mcmc(np.random.randn(nwalkers, ndim), nsteps)
            assert len(recorded_warnings) == 0


def run_sampler(
    backend,
    nwalkers=32,
    ndim=3,
    nsteps=25,
    seed=1234,
    thin=None,
    thin_by=1,
    progress=False,
    store=True,
):
    np.random.seed(seed)
    coords = np.random.randn(nwalkers, ndim)
    sampler = EnsembleSampler(nwalkers, ndim, normal_log_prob, backend=backend)
    sampler.run_mcmc(
        coords,
        nsteps,
        thin=thin,
        thin_by=thin_by,
        progress=progress,
        store=store,
    )
    return sampler


@pytest.mark.parametrize("backend", all_backends)
def test_thin(backend):
    with backend() as be:
        with pytest.raises(ValueError):
            with pytest.warns(DeprecationWarning):
                run_sampler(be, thin=-1)
        with pytest.raises(ValueError):
            with pytest.warns(DeprecationWarning):
                run_sampler(be, thin=0.1)
        thinby = 3
        sampler1 = run_sampler(None)
        with pytest.warns(DeprecationWarning):
            sampler2 = run_sampler(be, thin=thinby)
        for k in ["get_chain", "get_log_prob"]:
            a = getattr(sampler1, k)()[thinby - 1 :: thinby]
            b = getattr(sampler2, k)()
            c = getattr(sampler1, k)(thin=thinby)
            assert np.allclose(a, b), "inconsistent {0}".format(k)
            assert np.allclose(a, c), "inconsistent {0}".format(k)


@pytest.mark.parametrize(
    "backend,progress", product(all_backends, [True, False])
)
def test_thin_by(backend, progress):
    with backend() as be:
        with pytest.raises(ValueError):
            run_sampler(be, thin_by=-1)
        with pytest.raises(ValueError):
            run_sampler(be, thin_by=0.1)
        nsteps = 25
        thinby = 3
        sampler1 = run_sampler(None, nsteps=nsteps * thinby, progress=progress)
        sampler2 = run_sampler(
            be, thin_by=thinby, progress=progress, nsteps=nsteps
        )
        for k in ["get_chain", "get_log_prob"]:
            a = getattr(sampler1, k)()[thinby - 1 :: thinby]
            b = getattr(sampler2, k)()
            c = getattr(sampler1, k)(thin=thinby)
            assert np.allclose(a, b), "inconsistent {0}".format(k)
            assert np.allclose(a, c), "inconsistent {0}".format(k)
        assert sampler1.iteration == sampler2.iteration * thinby


@pytest.mark.parametrize("backend", all_backends)
def test_restart(backend):
    with backend() as be:
        sampler = run_sampler(be, nsteps=0)
        with pytest.raises(ValueError):
            sampler.run_mcmc(None, 10)

        sampler = run_sampler(be)
        sampler.run_mcmc(None, 10)

    with backend() as be:
        sampler = run_sampler(be, store=False)
        sampler.run_mcmc(None, 10)


def test_vectorize():
    def lp_vec(p):
        return -0.5 * np.sum(p ** 2, axis=1)

    np.random.seed(42)
    nwalkers, ndim = 32, 3
    coords = np.random.randn(nwalkers, ndim)
    sampler = EnsembleSampler(nwalkers, ndim, lp_vec, vectorize=True)
    sampler.run_mcmc(coords, 10)

    assert sampler.get_chain().shape == (10, nwalkers, ndim)


@pytest.mark.parametrize("backend", all_backends)
def test_pickle(backend):
    with backend() as be:
        sampler1 = run_sampler(be)
        s = pickle.dumps(sampler1, -1)
        sampler2 = pickle.loads(s)
        for k in ["get_chain", "get_log_prob"]:
            a = getattr(sampler1, k)()
            b = getattr(sampler2, k)()
            assert np.allclose(a, b), "inconsistent {0}".format(k)
