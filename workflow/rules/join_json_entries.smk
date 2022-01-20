rule join_json_entries:
    input:
        expand("json/pango_lineages.{n}.json", n=range(1,config["chunks"]+1)),
    output:
        "json/covid19-lineages.entries.json"
    shell:
        """
        cat {input} | head -n -1 > {output}
        """
