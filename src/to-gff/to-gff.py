#!/usr/bin/env python

# Copyright 2013-2014 Mitchell Stanton-Cook Licensed under the
# Educational Community License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may
# obtain a copy of the License at
#
#     http://www.osedu.org/licenses/ECL-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing
# permissions and limitations under the License.

"""
Generate gff file from EMBL/Genbank for QUAST
"""

__title__        = 'to_gff'
__version__      = '0.1'
__description__  = "Generate gff file from EMBL/Genbank for QUAST"
__author__       = 'Mitchell Stanton-Cook'
__license__      = 'ECL 2.0'
__author_email__ = "m.stantoncook@gmail.com"
__url__         = 'http://github.com/mscook/to_gff'


import sys, os, traceback, argparse
import time

from BCBio import GFF
from Bio import SeqIO

epi = "Licence: %s by %s <%s>" % (__license__,
                                  __author__,
                                  __author_email__)
__doc__ = " %s v%s - %s (%s)" % (__title__,
                                 __version__,
                                 __description__,
                                 __url__)

def to_GFF(args):
    """
    Convert a GenBank or EMBL file to GFF

    Mainly useful for QUAST (Quality Assessment Tool for Genome Assemblies)

    :param args: an argparse args list
    """
    args.in_file  = os.path.expanduser(args.in_file)
    args.out_file = os.path.expanduser(args.out_file)
    in_type = "genbank"
    if args.embl == True:
        in_type = "embl"
    if args.getfasta == True:
        base =  os.path.dirname(args.out_file)
        fasta = os.path.splitext(os.path.basename(args.out_file))[0]+'.fa'
        fasta_out =  os.path.join(base, fasta)
    with open(args.in_file) as fin, open(args.out_file, 'w') as fout:
        GFF.write(SeqIO.parse(fin, in_type), fout)
    if args.getfasta == True:
        with open(args.in_file) as fin, open(fasta_out, 'w') as opt_out:
            SeqIO.write(SeqIO.parse(fin, in_type), opt_out, "fasta")

if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = argparse.ArgumentParser(description=__doc__, epilog=epi)
        parser.add_argument('-v', '--verbose', action='store_true',
                                default=False, help='verbose output')
        parser.add_argument('--embl',action='store_true',
                                default=False, help=('Whether we have an '
                                                'EMBL or GenBank (default)'))
        parser.add_argument('--getfasta',action='store_true',
                                default=False, help=('Get a FASTA file '
                                    '(default = no)'))
        parser.add_argument('in_file', action='store',
                                help=('Full path to the input .embl/.gbk'))
        parser.add_argument('out_file', action='store',
                                help=('Full path to the output GFF'))
        parser.set_defaults(func=to_GFF)
        args = parser.parse_args()
        if args.verbose:
            print "Executing @ " + time.asctime()
        args.func(args)
        if args.verbose:
            print "Ended @ " + time.asctime()
            print 'Exec time minutes %f:' % ((time.time() - start_time) / 60.0)
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)
