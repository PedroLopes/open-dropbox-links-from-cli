# open-dropbox-links-from-cli
Opens the current directory on the Dropbox website using your web-browser

## how to install / use
Just add the files ``open-dropbox`` (a shell script) and
``open-dropbox.py`` (python) to your ``/usr/local/bin`` (or add them to your
``.bashrc``, etc.)

## using it
1. When you call ``./open-dropbox`` it will invoke the python script
   with the current dir (from executing ``pwd``)
2. The python script will launch your default way to open urls by
   calling ``open http:url-pointint-to-dropbox-and-path``
3. That should launch your browser (in a new tab) to the right place.
