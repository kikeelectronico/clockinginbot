# clockinginbot
A simple bot that sends me an email in order remember to clocking in

## Config

Crete a config file, name it _config.json_ and type the following content:

```
{
  "sender": "something@gmail.com",
  "password": "the_password",
  "smtp_server": "smtp.gmail.com",
  "smtp_port": 587,
  "imap_server": "imap.gmail.com",
  "receiver": "something@gmail.com",
  "resend_timeout": 60,
  "timeout": 300
}
```
