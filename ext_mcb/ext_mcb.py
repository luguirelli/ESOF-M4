import shelve,pyperclip,sys

ext_mcbShelf = shelve.open('ext_mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    ext_mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del ext_mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(ext_mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        for key in ext_mcbShelf:
            del ext_mcbShelf[key]
    elif sys.argv[1] in ext_mcbShelf:
        pyperclip.copy(ext_mcbShelf[sys.argv[1]])
ext_mcbShelf.close()