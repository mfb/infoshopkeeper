#!/usr/bin/python
# Copyright 2006 John Duda 

# This file is part of Infoshopkeeper.

# Infoshopkeeper is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or any later version.

# Infoshopkeeper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Infoshopkeeper; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301
# USA

from string import rjust,ljust
import sys

import components.db
conn=components.db.connect()

cursor=conn.cursor()


if len(sys.argv) == 1: 
	cursor.execute("SELECT * from transactionLog where action='SALE' order by date")
else:
	date=sys.argv[1]
	cursor.execute("SELECT * from transactionLog where action='SALE' and date like %s   order by date",(date+"%"))


rows=cursor.fetchall()

total = 0

for r in rows:
	price = r[1]
	total=total + r[1]
	price_string = rjust("%.2f" % r[1],10)
	print "%s | %s | %s" % (r[2],ljust(r[4][:100],50),price_string)


print
print "Total Sales:  %.2f" % total
