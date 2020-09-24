from notebook.auth import passwd;


import sys;print('c.NotebookApp.password = ', '"', passwd(sys.argv[1]), '"', sep='')