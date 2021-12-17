rule run_pangolin:
    input:
        "sequences/pango_seqs.{n}.fasta"
    output:
        "pango/pango_lineages.{n}.csv"
    shell:
        "pangolin --threads 1 --outfile {output} {input}"
