# Wiki documentation

General: a clear, step-by-step walkthrough of all the parts required for making a custom app is missing. Most of the parts are there, but it's not entirely obvious 

## Install instructions

* do not make users add the virtual env activation to their bashrc — then every time they open a terminal they will automatically have the oTree environment which is probably not what they want. Or at least, warn them about what you are doing there. It would be better to include instructions on how to activate the shell without making it the default
* there can be problems with the OS-shipped python under MacOS — perhaps a recommendation for free python distributions like anaconda python or enthought canopy python would be good
* consider making a conda package?
* a bit confusing to have “Setup” in two places — on the first page of the wiki, as well as in the sidebar. They are quite different — perhaps the one on the main page should just link to https://github.com/oTree-org/oTree/wiki/Setup
* Setup steps need to be taken *after* the prerequisites have been done —> on the front page of the wiki this is not the case
* an IDE is not a requirement — some users may prefer not to have one
* is the “setup” wiki page assuming that the user is cloning and installing dependencies with the virtual env activated? This should be made explicit. 

## Sessions

* Defaults for ``SessionType`` are not listed 
* the section "Players vs. Participants" seems out of place -- I understand it has to do with subsessions, but this link is not made clear so it is confusing on first read
* use some sort of syntax coloring here to make clear which parts are just words, e.g. "a participant is a person who takes part in a session" vs. "Each player has a ``participant`` attribute"

## Apps

* Django complains about Raven not  being configured -- does this matter? 
* experiments are no longer in the hierarchy shown on the "Apps" page -- the ``otree_experiments`` subdirectory seems to  not exist; the ``static`` and ``templates`` directories are not created for the app (this probably doesn't matter)
* the ``./otree startapp your_app_name`` command doesn't add a default HTML template -- would be nice if it did? 

## Models

This page could really be split into two parts: 
1. an illustrative example on how to construct models for a simple use case
2. a "reference" section that explains a few more details about the different parts of ``models.py`` file. 

Validation: strange formatting with header-style used together with code text?

minor: the table should probably be a regular markdown table? 

## Test Bots

How do the bots get assigned to different groups? 

## Admin

* add a note that tells you how to clean up the sessions? (i.e. remove them from the list in ``sessions.py``)
* add some user interface pointers
* is there a way to use bots to see how the admin interface functions with fake participants? 



