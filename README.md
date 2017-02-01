# nagios2statuspage
Nagios Notifier to update a StatusPage.io component

This simple command line tool converts a nagios state to statuspage.io component state format before calling the api.
Example config in statuspage.cfg

How To Use:
1. Make statuspageupdate.py available to the nagios user
2. Put statuspage.cfg nagios in a nagios include path, or copy the bits needed from example
3. Change the values for _SP_API_KEY, _SP_PAGE_ID, _SP_LOG, _SP_COMPONENT_ID(s) as appropriate
4. Set contact_groups within the monitored thing definition to include YOUR new statuspage contact