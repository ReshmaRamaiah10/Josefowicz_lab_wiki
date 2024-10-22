Usage
=====

.. _installation:

Installation
------------

To use Josefowicz_lab, first install it using pip:

.. code-block:: console

   (.venv) $ pip install Josefowicz_lab

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``Josefowicz_lab.get_random_ingredients()`` function:

.. autofunction:: Josefowicz_lab.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`Josefowicz_lab.get_random_ingredients`
will raise an exception.

.. autoexception:: Josefowicz_lab.InvalidKindError

For example:

>>> import Josefowicz_lab
>>> Josefowicz_lab.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

