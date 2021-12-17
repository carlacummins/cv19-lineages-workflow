import sys, re
import argparse
import subprocess
import math

parser = argparse.ArgumentParser()
parser.add_argument('--embl', help="input file in embl format", required=True)
parser.add_argument('--num', help="number of output files required", required=True)
parser.add_argument('--outdir', help="path to output directory", required=True)
opts = parser.parse_args(sys.argv[1:])

total_seqs = subprocess.check_output("grep -c '^//' {}".format(opts.embl), shell=True)
total_seqs = int(total_seqs)
seqs_per_file = math.ceil(total_seqs/int(opts.num))
print(f"Found {total_seqs} in {opts.embl} - writing {seqs_per_file} to each file")

capture_sequence = False
file_num = 1
base_path = opts.outdir

this_outfile = "{}/pango_seqs.{}.fasta".format(base_path, file_num)
outfile = open(this_outfile, 'w')

file_contains, captured_seqs = 0, 0
this_acc, this_seq = '', ''
with open(opts.embl, 'r') as embl_file:
    for line in embl_file:
        if re.search('^[\/\=]{2}', line):
            capture_sequence = False
            if len(this_seq) > 0:
                outfile.write(f">{this_acc}\n")
                outfile.write(f"{this_seq}\n")
                # print("writing {} : {} (len:{}) to {}".format(this_acc, this_seq[:10], len(this_seq), this_outfile))
                file_contains += 1
                captured_seqs += 1
                this_seq = ''

            if file_contains == seqs_per_file:
                file_num += 1
                outfile.close()
                this_outfile = "{}/pango_seqs.{}.fasta".format(base_path, file_num)
                outfile = open(this_outfile, 'w')
                file_contains = 0

            if captured_seqs % 2500 == 0:
                print("Captured {} sequences...".format(captured_seqs))

        elif capture_sequence:
            # clean the sequence
            while re.search('[\s\d]+', line):
                line = re.sub('[\s\d]+', '', line)
            this_seq += line

        # if not in sequence capture mode, check for accession
        ac_rx = re.search('^AC\s+([\w]+)', line)
        if ac_rx:
            this_acc = ac_rx.group(1)
            continue

        # or check if sequence capture should begin
        sq_rx = re.search('^SQ', line)
        if sq_rx:
            capture_sequence = True
            continue

outfile.close()
