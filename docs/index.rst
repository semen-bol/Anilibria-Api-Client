anilibria-api-client Documentation
==================================

Python async API wrapper for AniLibria Swagger

.. toctree::
   :maxdepth: 3
   :caption: API Reference

   api/models
   api/types
   api/api_client
   api/exceptions
   api/helper

.. toctree::
   :maxdepth: 2
   :caption: Guides

   getting_started
   examples

Quick Example
-------------

.. code-block:: python

   from anilibria_client import AsyncAnilibriaAPI # Client
   from anilibria_client.exceptions import AnilibriaException, AnilibriaValidationException # Errors
   from anilibria_client.types import * # Types for some methods
   from anilibria_client.models import * # Models for some methods
   from anilibria_client.helper import * # Download anime, save torrents files and more

   async def main():
      async with AsyncAnilibriaAPI() as api: # async with
         await api.teams.users(include="nickname")

      api = AsyncAnilibriaAPI() # like js support
      await api.teams.users(include="nickname")

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`