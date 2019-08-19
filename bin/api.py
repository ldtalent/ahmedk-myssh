#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
import argcomplete
import argparse
import requests
import pprint
from sqlalchemy.orm import sessionmaker
from ssh_app.models import Base, SSHEntry
from sqlalchemy import create_engine
engine = create_engine('sqlite:////home/ahmmkh/myssh/ssh.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def name_completer(prefix, parsed_args, **kwargs):
    listt = [i.name for i in  session.query(SSHEntry).all()]
    return (i for i in listt)


parser = argparse.ArgumentParser()
parser.add_argument(
    "--name", help="GitHub member").completer = name_completer

argcomplete.autocomplete(parser)
args = parser.parse_args()
print args


