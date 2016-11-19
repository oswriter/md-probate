# md_probate -- Maryland Probate Fees Calculator
# v. 2.1 (2016-11-18)
# Based on Md. Estates and Trusts secs. 2-206 & 7-601
#
# (C) 2016 S.M. Oliva <oswriter@skipoliva.com>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. The name of the author may not be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR "AS IS" AND ANY EXPRESS OF IMPLIED
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
#
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, 
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING BUT
# NOT LIMITED TO PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

message = "Welcome to the Maryland Probate Fees Calculator"
message +="\nby S.M. Oliva <skip@skipoliva.com>"
message +="\nThis program is published under a BSD License."
message +="\n\nPlease enter a dollar amount without any currency symbols ($) or commas (,)."
print(message)

while True:
    gross_estate = input("\nWhat is the value of the decedent's Maryland gross estate? ")

    try:
        gross_estate = int(gross_estate)
    except ValueError:
        print("Please enter a dollar amount without any currency symbols ($) or commas (,).")
    else:
        break
                  
# Calculation of Probate Fees under Md. Estates and Trusts sec. 2-206(b)(2),
# for estates of decedents dying on or after 7/1/1989.

if gross_estate < 0:
    fee = "$0.00"
elif gross_estate < 10000:
    fee = "$50.00"
elif gross_estate < 20000:
    fee = "$100.00"
elif gross_estate < 50000:
    fee = "$150.00"
elif gross_estate < 75000:
    fee = "$200.00"
elif gross_estate < 100000:
    fee = "$300.00"
elif gross_estate < 250000:
    fee = "$400.00"
elif gross_estate < 500000:
    fee = "$500.00"
elif gross_estate < 750000:
    fee = "$750.00"
elif gross_estate < 1000000:
    fee = "$1,000"
elif gross_estate < 2000000:
    fee = "$1,500"
elif gross_estate < 5000000:
    fee = "$2,500"
else:
    fee = 2500 + (0.0002 * (gross_estate - 5000000))
    fee = locale.currency( fee, grouping=True )

print("\nThe Maryland probate fee for this estate is " + fee + ".")

# Calculation of PR's Commissions and/or Attorney's Fees
# under Md. Estates and Trusts  sec. 7-601(b),
# for estates of decedents dying on or after 1/1/1992.

if gross_estate < 0:
    comm = 0
elif gross_estate < 20000:
    comm = .09 * gross_estate
else:
    comm = 1800 + (0.036 * (gross_estate - 20000))

comm = locale.currency( comm, grouping=True )

message = "The maximum personal representative's commission and/or attorney's fees for this estate is " + comm + "."
print(message)
