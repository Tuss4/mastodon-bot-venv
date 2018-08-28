from mastodon import Mastodon

mdon = Mastodon(
    access_token = 'token.secret',
    api_base_url = 'https://botsin.space/')

mdon.status_post("It's yah boi Val-Zod!")
