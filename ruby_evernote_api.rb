#!/usr/bin/env ruby
#Copyright DSK 2013
require 'evernote_oauth'

auth_token = "S=s1:U=6052d:E=1449ab513dc:C=13d4303e7dc:P=1cd:A=en-devtoken:V=2:H=1f993da85f6e932c18f1295bf9fda3fe"

client = EvernoteOAuth::Client.new(token: auth_token)
note_store = client.note_store
notebooks = note_store.listNotebooks
note = Evernote::EDAM::Type::Note.new(title: "Hello from Codecademy")
note.content = '<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">
<en-note>Hello Evernote<br/></en-note>'

note_store.createNote(note)
