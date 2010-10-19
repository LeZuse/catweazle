'''
``hama`` is the top level module of the whole package. It also imports all entry-point functions for easier access from the setup.py script

==========

.. _e_p_hamacase:
.. autofunction:: hama_case_cli

..
    ==========

    .. _e_p_guppy:
    .. autofunction:: guppy

    ==========

    .. _e_p_grimble:
    .. autofunction:: grimble

    ==========

    .. _e_p_jimbo:
    .. autofunction:: jimbo

    ==========

    .. _e_p_eugene:
    .. autofunction:: eugene

    ==========

    .. _e_p_update_e_presenter:
    .. autofunction:: update_e_presenter
'''
from hama.cli.hamacase_cli import hama_case_cli
from hama.cli.eugene import eugene
from hama.cli.update_e_presenter import update_e_presenter
from hama.cli.grimble import grimble
from hama.cli.guppy import guppy
from hama.cli.jimbo import jimbo
