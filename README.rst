=========================
 Let's Write a Database!
=========================

OK! So there are obviously not enough databases out there, especially
silly command line, key/value databases that support made up query
languages. We need to write one.


Here's How it Works
===================

This projects contains barely a skeleton for how this can work. It
handles some of the command line bits so you can focus on adding
functionality and features.

To get started:

 1. Fork and clone the repo
 2. Create a branch
 3. Write a database!!!!
 4. Submit a Pull Request

If you have any questions or want to discuss anything, hop on irc.freenode.net and
ask `elarson` in #openstack-dns or send an email (eric.larson (at)
rackspace.com).


What Kind of Database Should I Write?
=====================================

It is up to you! With that said, here are some constraints to keep you
sane.

 1. Keys must be strings and command line friendly.
 2. Values must be valid JSON
 3. Queries return a list of keys
 4. Don't use any storage / db that is not in the standard library
 5. Written in Python
 6. **At least implement the `set`, `get` and `rm` commands**

Here is what it (might) look like when you're done:

.. code-block:: bash

   # Create / Update
   $ iwadb set foo '{"msg": "hello world"}'

   # Read
   $ iwadb get foo
   {"msg": "hello world"}

   # Delete
   $ iwadb rm foo

   # Query
   $ iwadb query $your_query_language
   foo  <- we found the key 'foo'

   # Add an index
   $ iwadb index $your_index_or_query_language

Now, don't spend a **ton** of time on this. The goal is not to have a
perfectly functioning database, but rather, have a little fun on a toy
project that helps you show off your Python skills. Try to limit
yourself to an hour or two max. Feel free fill in any gaps in the
Design and Usage sections below.

We'll be asking questions, so don't feel as though once that pull
request is submitted that's it. You can always update your pull
request. Release early, release often! We want to see your development
process, not perfection.


Getting Started Writing Code
----------------------------

Once you've checked out your clone and created your branch, here is
how you can get started running the existing code.

.. code-block:: bash

   # Create a virtualenv
   $ virtaulenv venv

   # Activate the virtualenv
   $ source venv/bin/activate

   # Install the current package
   $ pip install -e .

This will install the `iwadb` command (do you know how that
happend?). The project skeleton uses the `click
<http://click.pocoo.org/>`_ library to provide command line support. Feel
free to use it, extend or even replace it if you have a better tool.


Design
======

Fill this in with anything you'd like us to know about your
implementation or what you'd like to implement given a ton of time.


Usage
=====

Let us know how best to play with your submission! Run the tests? A
script? List some commands below? Whatever works!

Do you have anything you'd like to work but doesn't yet? Add it here!


Thanks!
=======

Thanks for taking on this challenge. We hope it is fun. There are no
wrong answers here. It is an opportunity to show off your skills in an
environment where you're comfortable.
