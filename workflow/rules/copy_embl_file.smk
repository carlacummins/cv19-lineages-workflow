rule copy_embl_file:
    input:
        "{embl_input}"
    output:
        "embl-covid19.dat"
    shell:
        "cp {input} {output}"
