# Mastodon Bot Venv

Pretty much fork this and have fun. Just be sure to create your `token.secret` file as described in the [tutorial by Terence Eden](https://shkspr.mobi/blog/2018/08/easy-guide-to-building-mastodon-bots/#comment-58272)

Make an `env/` folder in the same directory as these files then run:
```
python3 -m venv env
```

When ready activate your virtual env:
```
. env/bin/activate
```

Install your dependencies:
```
pip3 install -r requirements.txt
```

Run the script:
```
python3 bot.py
```

Boom.
