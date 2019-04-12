{%- capture examples -%}
"add_tags": [
    "volunteer",
    "donor"
],
"add_lists": [
    "supporters"
],
"add_questions_responses_uri": [
  {
    "question": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29",
    "responses": [ "r1", "r2", "r2"]
  }
]{%- endcapture -%}
{%- assign examples_lines = examples | newline_to_br | strip_newlines | split: '<br />' -%}
{% for line in examples_lines %}{{ line | prepend: include.prefix }}
{% endfor %}