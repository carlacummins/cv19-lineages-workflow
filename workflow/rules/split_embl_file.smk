rule split_embl_file:
    input:
        embl = "embl-covid19.dat"
    output:
        expand("sequences/pango_seqs.{n}.fasta", n=range(1,config["chunks"]+1))
    params:
        num = str(config["chunks"])
    shell:
        "python workflow/scripts/split_embl_file.py --embl {input.embl} --num {params.num} --outdir sequences/"
