"""import sys
import oursql
try:
    conn = oursql.connect (host = "localhost", user = "root",
    passwd = "passwd", db = "test")
except oursql.Error, e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit (1)
"""