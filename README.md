# clockinginbot
A simple bot that sends me an email in order remember to clocking in

## Config file

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

## Setup

Create as many cronjobs as needed in order to run the script every time you need it. For example, you can run it at 09:00 on every day-of-week from Monday through Friday using a cronjob like ```0 9 * * 1-5```. 
