{%- capture districts_examples -%}
"division_info" : [
  {
    "name": "State",
    "divisions": [
      {
        "id": "OH",
        "name": "Ohio",
        "ocd_id": "ocd-division/country:us/state:oh"
      }

    ]
  },
  {
    "name": "Congressional",
    "divisions": [
      {
        "id": "012",
        "name": "Ohio 12th Congressional District",
        "ocd_id": "ocd-division/country:us/state:oh/cd:12"
      }

    ]
  }
],
{%- endcapture -%}
{%- assign districts_examples_lines = districts_examples | newline_to_br | strip_newlines | split: '<br />' -%}
{% for line in districts_examples_lines %}{{ line | prepend: include.prefix }}
{% endfor %}