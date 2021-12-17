rule make_json_header_footer:
    input:
        "embl-covid19.dat",
    output:
        template = "json/covid19-lineages.temp.json",
        header = "json/covid19-lineages.header.json",
        footer = "json/covid19-lineages.footer.json"
    shell:
        """
        python {basedir}/scripts/generate_json_template.py {input} > {output.template};
        head -6 {output.template} > {output.header};
        tail -3 {output.template} > {output.footer};
        """
