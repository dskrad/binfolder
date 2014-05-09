# Plugin related mappings

## Open bufexplorer and see and manage the current buffers:
    map <leader>o :BufExplorer<cr>

## Open and manage tabs
    map <leader>tn :tabnew<cr>
    map <leader>tc :tabclose<cr>
    map <leader>to :tabonly<cr>
    gt (goto next tab) 
    gT (goto prev tab)

## Surround the visual selection in parenthesis/brackets/etc.:
    vnoremap $1 <esc>`>a)<esc>`<i(<esc>
    vnoremap $2 <esc>`>a]<esc>`<i[<esc>
    vnoremap $3 <esc>`>a}<esc>`<i{<esc>
    vnoremap $$ <esc>`>a"<esc>`<i"<esc>
    vnoremap $q <esc>`>a'<esc>`<i'<esc>
    vnoremap $e <esc>`>a"<esc>`<i"<esc>

## Spell checking
Pressing <leader>ss will toggle and untoggle spell checking

    map <leader>ss :setlocal spell!<cr>

Shortcuts using <leader> instead of special chars

    map <leader>sn ]s
    map <leader>sp [s
    map <leader>sa zg
    map <leader>s? z=

## Open MRU.vim and see the recently open files:
    map <leader>f :MRU<CR>

## Open ctrlp.vim plugin:
    let g:ctrlp_map = '<c-f>'

## Once CtrlP is open:
    <F5> to purge the cache for the current directory to get new files, remove deleted files and apply new ignore options.
    <c-f> and <c-b> to cycle between modes.
    <c-d> to switch to filename only search instead of full path.
    <c-r> to switch to regexp mode.
    <c-j>, <c-k> or the arrow keys to navigate the result list.
    <c-t> or <c-v>, <c-x> to open the selected entry in a new tab or in a new split.
    <c-n>, <c-p> to select the next/previous string in the prompt's history.
    <c-y> to create a new file and its parent directories.
    <c-z> to mark/unmark multiple files and <c-o> to open them.
    
    :help ctrlp-mappings or submit ? in CtrlP for more mapping help.

    .. to go up the directory tree by one or multiple levels.
    End the input string with a colon : followed by a command to execute it on the opening file(s):
    :25 to jump to line 25.
    :diffthis when opening multiple files to run :diffthis on the first 4 files.

## Open PeepOpen plugin:
    map <leader>j :PeepOpen<cr>

## Managing the NERD Tree plugin:
    map <leader>nn :NERDTreeToggle<cr>
    map <leader>nb :NERDTreeFromBookmark 
    map <leader>nf :NERDTreeFind<cr>
