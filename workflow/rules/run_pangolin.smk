rule run_pangolin:
    input:
        "sequences/pango_seqs.{n}.fasta"
    output:
        "pango/pango_lineages.{n}.csv"
    threads: 4
    resources:
        mem_mb = 2048
    shell:
        "pangolin --threads {threads} --outfile {output} {input}"
