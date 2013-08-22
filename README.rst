Generate GFF file from EMBL/Genbank
===================================

This tool makes it easy to get a .fa and .gff from input GenBank or EMBL 
files.

QUAST: Quality Assessment Tool for Genome Assemblies 
(http://bioinf.spbau.ru/quast) wants references and genes in FASTA format and 
GFF respectively. Most often our internal completed/closed strains are 
**only**  available in GenBank or EMBL format.


Usage
-----

Something like::

    ./to-gff -h
    usage: to-gff [-h] [-v] [--embl] [--getfasta] in_file out_file

    to_gff v0.1 - Generate gff file from EMBL/Genbank for QUAST
    (http://github.com/mscook/to_gff)

    positional arguments:
      in_file        Full path to the input .embl/.gbk
      out_file       Full path to the output GFF

    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  verbose output
      --embl         Whether we have an EMBL or GenBank (default)
      --getfasta     Get a FASTA file (default = no)

    Licence: ECL 2.0 by Mitchell Stanton-Cook <m.stantoncook@gmail.com>


Examples
--------

Example usage::

    #(get ~/EC958.gff)
    $ ./to-gff ~/st131_100/ec958.pacbio.annotation-v10.embl ~/ec958.gff --embl

    #(get ~/EC958.gff)
    $ ./to-gff ~/st131_100/ec958.pacbio.annotation-v10.embl ~/ec958.gff

    #(get ~/EC958.gff & EC958.fa)
    $ ./to-gff ~/ST131_100/EC958.pacbio.annotation-v10.embl ~/EC958.gff --embl --getfasta


Requirements
------------

Requires following (thanks to the authors):
    * bcbio-gff>=0.2
    * biopython>=1.62b
