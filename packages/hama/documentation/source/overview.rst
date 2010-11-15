========
Overview
========

Catweazle [#catweazle]_ is a set of utilities designed to make certain tasks easier or more efficient. It is achieved by leaving repetitive tasks that don't need human supervision to the computer. Leaving them to computer does not mean they can only be carried out automatically. Everything Catweazle does can be achieved manually as well (with a little help of the computer, office suite, internet browser and simple image editor). This means that there is always a fallback plan.

Catweazle contains tools ranging from image sourcing to the ePresenter updating. You will find the full list in the :ref:`next section <catweazle_tools>`. Each of these tools is dedicated to one specific task. As a result, there is quite a lot of them and it might be difficult to find the right one (if available at all) for particular job.

This document was designed to help you to pick the right tool and to learn everything important about it. To use the help system efficiently please read few following paragraphs. They should explain, how to navigate the help system and how it is organised. 


Help on Help
============
Whole help system is, in fact, an HTTP document and you cannot go wrong if you treat it like any other web page. You can click the hyper links, use your browser's ``back`` button or create bookmarks. All pages use different layout for display and printing [#printing]_. Certain navigational features can also be used via their hot key [#accesskey]_. In following text I will mention them in this form: ``accesskey + a``.

When starting to browse the help document, you are presented with the :ref:`table of contents <toc>`. It shows you structure of the whole document. Each entry is hyper linked to the relevant part of the document. If you ever lose your way and want to return back use link in the sidebar saying ``Table Of Contents``.

You may prefer to read the whole documentation in its intended order instead of jumping through the hyperlinks. In this case follow the links in the sidebar labeled *Previous topic* ``accesskey + p`` or *Next topic* ``accesskey + n``. This is not unlike turning pages in a book. You are guaranteed to read every section of this document.

This help system also features index functionality. You can get to it by using the ``index`` link in right top corner or ``accesskey + i``.


Where to Look
=============

All information presented here is organised in couple of sections for easier navigation. Let us have a quick overview in the following breakdown:

1. :ref:`Frequently Asked Questions <faq>`:

   Chances are that your problem has been solved cople of times before.

#. :ref:`User Guide <User Guide>`:

   This section lists all program that are installed on your computer with Catweazle. They are not ordered by any specific key. Each entry contains a short description, usage example and warning about possible gotchas. Go here, if you don't know how to use certain function, or if you want to find what can Catweazle offer you.

#. :ref:`Administrator Guide <Administrator Guide>`:
   
   You can find high level overview of the whole system, Installation guide and quick primer about editing the help system. Go here, if you want to install Catweazle on a fresh system, or if you need to update the Help files. You should at least skim through the :ref:`User Guide <User Guide>` before going here.

#. :ref:`Developer Guide <Developer Guide>`:
   
   Under-the-bonnet view. You can find description of the Python code that drives the external programs. This section expects good understanding of all subjects dealt with in both :ref:`User Guide <User Guide>`: & :ref:`Administrator Guide <Administrator Guide>`.

#. :ref:`genindex`:

   Index page works exactly like an index in the book. If you feel that certain part of this help was wrongfully excluded from index please refer to :ref:`Administrator Guide <Administrator Guide>` on how to add an index entry.

#. :ref:`search`:
   
   Search by key words. The text field in the sidebar labeled *Quick search* does the very same thing. Please note that it only finds pages containing **all key words**, so try not to make your searches too narrow or you'll end up with no results.

#. **Contact me**:

   If all fails `contact the author <mailto:mhrdina@hama.co.uk?subject=Catweazle%20Documentation%20Issue>`_.

-----

.. rubric:: Footnotes

.. [#catweazle] I felt it more appropriate to go for arbitrary names instead of descriptive ones. After all *Catweazle* is easier to remember than *this_here_system_that_can_do_a_lot*. All credits for (unknowingly) suggesting this name go to Mr Les Morris, who mentioned his favourite children TV series of the same name just when I was trying to come up with something.

.. [#printing] Although it makes this documentation printer friendly, it is not recommended to print pages for long term reference. Your printed pages will become obsolete whenever this documentation is updated. 

.. [#accesskey] ``accesskey`` is implemented differently for each browser. Please refer to http://en.wikipedia.org/wiki/Access_key for more info