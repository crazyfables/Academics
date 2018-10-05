# By Jessica Angela Campisi
# Guess My Number
# 10/04/2018
# Description: Practice Twisted file

from __future__ import print_function

import sys

from twisted.internet import protocol, defer, endpoints, task
from twisted.mail import imap4
from twisted.python import failure

@defer.inlineCallbacks
def main(reactor, username=b''):
    print("")
