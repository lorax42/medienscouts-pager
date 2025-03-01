# medienscouts-pager

Pager system for the Medienscouts at our school

## Folder Structure

<pre>
./
├ pager/
│ ├ circuit/
│ │ └ ...
│ ├ code/
│ │ └ ...
│ └ README.md
├ server/
│ ├ README.md
│ ├ setup.sh
│ └ ...
├ CONTRIBUTING.md
├ LICENSE
└ README.md
</pre>

## Background

* _Medienscouts_ club at our school
  * do tech stuff for school and ourselves
* some teachers have trouble with tech at school
  * eg. projectors, laptops, etc.
* we need new members - how advertise?
-> club members could be called to help
* this would help the teachers and also advertise the club

* how do teachers reach us?
-> **Pagers**

## Sequence Plan

* teacher who needs help sends Email to Pager server's LernSax adress
* server pulls down Emails periodically and checks for new entries
* if new Email is recognized the server serves the Email Subject to web API
    (via IP-Adress on school WiFi)
* pager periodically polls web API, reads message, beeps and displays it

### Server

<!-- * fetchmail + procmail -->
* python libs

#### Future

* execute mapped commands if email is from a specific user and has a trigger
    word in Subject
  * eg. `SCOUTDO: add <IP-Adress>` to add a pager to the system
  * this message isn't sent to the Pagers
  * maybe reply to the email with an info message

### Pager

* ESP32
* LCD screen
  * display battery level, wifi status
* status light
* power button
* loadable battery

#### Future

* mute button
  * display status on screen
* Ok button to accept a message
  * tell server -> server tells other pagers someone has already read the
      message
* SDCard for logs, configs

## Features

* none so far

## TODO

* basic implementation
