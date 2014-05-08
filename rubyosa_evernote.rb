#!/usr/bin/env ruby
#Copyright DSK 2013

require "rubyosa"
require "rubygems"

en = OSA.app('Evernote')
args = {:title => "hello from rbosa", :with_text => "hello", 
  :notebook => "drdsk's notebook", :tags => []}
en.create_note(args)

# create note v : Create a new note. You must specify exactly one of 'from file', 'from url', 'with text', or 'with html'.
#   create note
#   [from file file] : Clip the contents of the specified file.
#   [from url text] : Clip the contents of the specified URL.
#   [with text text] : Create a new note using the specified plain-text as content.
#   [with html text] : Create a new note using the specified html as content.
#   [with enml text] : Create a new note using the specified ENML as content. Do not include the <en-note> tags, only what should be between them.
#   [title text] : Title for the new note.
#   [notebook text or notebook] : Notebook in which to place the note. Can be the name of a notebook or an object reference. If no notebook with the specified name exists a new one is created. If no notebook is specified, the default notebook for the account is used.
#   [tags list of text or list of tag] : Tags to assign to the new note. Can be the name of a tag or an object reference. If no tag with the specified name exists a new one is created.
#   [attachments list of file] : Files to attach to the note.
#   [created date] : Creation date for the new note. Defaults to now.
#   → note : The new note.
