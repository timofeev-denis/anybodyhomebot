# Python Telegram Bot

### Required packages

- pip install requests
- pip install emoji --upgrade

### Registering WebHook

```shell
BOT_TOKEN=replace_with_your_token

BOT_PUBLIC_URL=https://$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE 's/.*public_url":"https:..([^"]*).*/\1/p')

curl --location --request POST 'https://api.telegram.org/bot'"$BOT_TOKEN"'/setWebhook' \
--header 'Content-Type: application/json' \
--data-raw '{
"url": "'"$BOT_PUBLIC_URL"'"
}'
```
