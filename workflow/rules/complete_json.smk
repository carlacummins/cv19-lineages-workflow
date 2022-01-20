rule complete_json:
    input:
        entries = "json/covid19-lineages.entries.json",
        header = "json/covid19-lineages.header.json",
        footer = "json/covid19-lineages.footer.json"
    output:
        "covid19-lineages.json"
    shell:
        """
        cat {input.header} {input.entries} {input.footer} > {output};
        rm {input.entries}
        """
