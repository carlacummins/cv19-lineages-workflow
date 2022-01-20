rule convert_to_json:
    input:
        "pango/pango_lineages.{n}.csv"
    output:
        "json/pango_lineages.{n}.json"
    shell:
        "python workflow/scripts/pangolin_to_ebi_search.py {input} > {output}"
