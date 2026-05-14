face-recognition-models-ng
==========================

.. note::

   **This is a maintained fork of** `ageitgey/face_recognition_models <https://github.com/ageitgey/face_recognition_models>`__,
   which appears to be no longer actively maintained. It is a companion package to
   `face-recognition-ng <https://github.com/jucasansao/face_recognition>`__.

This package contains only the trained model files used by
`face-recognition-ng <https://github.com/jucasansao/face_recognition>`__.

These models were created by `Davis King <https://github.com/davisking/dlib-models>`__ and are
licensed in the public domain or under CC0 1.0 Universal. See LICENSE.

Installation
------------

.. note::

   This package **cannot be published to PyPI** because the model files (~128 MB total)
   exceed PyPI's 100 MB per-release limit. Install directly from GitHub:

.. code:: bash

    pip install git+https://github.com/jucasansao/face_recognition_models.git

Changes from upstream
---------------------

- **Packaging**: Migrated to PEP 517/518/621 ``pyproject.toml``. ``setup.py`` and
  ``MANIFEST.in`` removed.
- **Python support**: Dropped Python 2 and Python < 3.9. Targets Python 3.9–3.14.
- **Dependencies**: Replaced deprecated ``pkg_resources.resource_filename`` (setuptools)
  with ``importlib.resources.files`` (stdlib, Python 3.9+). No runtime dependencies.
- **CI**: Replaced Travis CI with GitHub Actions; matrix covers 3.9–3.14. CI verifies
  all four model paths resolve to real files after install.
- **Modernisation assistance**: Packaging modernisation in this fork was assisted by
  `Claude Code <https://claude.ai/code>`__ (Anthropic).
