icap_server
==============

This is a ICAP server writen in python with pyicap framework.

The ideia is to do a plugin based ICAP server easy to extend and learn.

This is a very early project, not even alpha,

I'm not a very talented programmer, so, I need help to go alpha!

To test:

1) Configure squid:
icap_enable on
icap_preview_enable off
icap_send_client_ip on
icap_send_client_username on
icap_service reqmod reqmod_precache bypass=1 icap://127.0.0.1:1344/reqmod
icap_service respmod respmod_precache bypass=1 icap://127.0.0.1:1344/respmod

2) Start the server:
$ ./icap_server.py ./icap_server.cfg

3) Point you browser to use squid

4) Enjoy!

TODO:
 - Implement ICAP preview
 - Change the log system (rewrite the pyicap log)
 - many others... :)
