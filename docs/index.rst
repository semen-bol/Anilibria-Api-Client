AniLibria-Api-Client Documentation
==================================

Python async API wrapper for AniLibria Swagger

Example
-------------

.. code-block:: python

   from anilibria_client.api_client import AsyncAnilibriaAPI # Client
   from anilibria_client.exceptions import AnilibriaException, AnilibriaValidationException # Errors
   from anilibria_client.types import * # Types for some methods
   from anilibria_client.models import * # Models for some methods
   from anilibria_client.helper import * # Download anime, save torrents files and more

   async def main():
      async with AsyncAnilibriaAPI() as api: # async with
         await api.teams.users(include="nickname")

      api = AsyncAnilibriaAPI()
      await api.teams.users(include="nickname")

.. toctree::
   :maxdepth: 4
   :caption: Pages:

   pages.rst