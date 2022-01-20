rule copy_embl_file:
    input:
        config["embl_input"]
    output:
        "embl-covid19.dat"
    shell:
        "cp {input} {output}"
