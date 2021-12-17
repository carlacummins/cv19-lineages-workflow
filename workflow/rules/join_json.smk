rule join_json:
    input:
        entries = expand("json/pango_lineages.{n}.json", n=range(1,config["chunks"]+1)),
        header = "json/covid19-lineages.header.json",
        footer = "json/covid19-lineages.footer.json"
    output:
        "covid19-lineages.json"
    shell:
        """
        cat {input.entries} | head -n -1 > json/covid19-lineages.entries.json
        cat {input.header} json/covid19-lineages.entries.json {input.footer} > {output}
        rm json/covid19-lineages.entries.json
        """
