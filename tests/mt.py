from anilibria_client import AsyncAnilibriaAPI

api = AsyncAnilibriaAPI()

async def all_methods():
    await api.accounts.otp_accept()
    await api.accounts.otp_get()
    await api.accounts.users_auth_login()
    await api.accounts.users_auth_logout()
    await api.accounts.users_auth_password_forget()
    await api.accounts.users_auth_password_reset()
    await api.accounts.users_auth_social_authenticate()
    await api.accounts.users_auth_social_login()
    await api.accounts.users_me_collections_references_age_ratings()
    await api.accounts.users_me_collections_references_genres()
    await api.accounts.users_me_collections_references_types()
    await api.accounts.users_me_collections_references_years()
    await api.accounts.users_me_collections_ids()
    await api.accounts.users_me_collections_releases_get()
    await api.accounts.users_me_collections_releases_post()