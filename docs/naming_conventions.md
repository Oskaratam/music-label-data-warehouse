--------
File purpose: Clearly define all the naming conventions for objects in the project 
Objects: file names, database tables/views/columns/procedures/triggers, docs
--------

**General Conventions**

***Naming style*** - snake case, with lower case letters with '_' underscore to separate the words 
***Language*** - English
***Script names*** - <Abbreviated layer name>_<script purpose>.<extension>
'Abbreviated layer name' reprsents shortened name of the data processing stage where the script is applied (e.g., bronze - brz, silver - slv, gold - gd)
Examples: brz_load_json.py, gd_ddl.sql

**Docs Conventions**

***Visualization based docs*** - <order>_<artifact_type>_<description>.<extension>
Examples - 01_architecture_layers.drawio, 03_model_star_schema.png, 02_architecture_data_flow.drawio

***Text based docs*** - <descriptive name using the general naming style>.<extension>
Examples: model_evaluation.md, data_dictionary.md

***Standard Top-Level Files*** - <descriptive name all caps>.<extension>
Examples: README.md, CONTRIBUTING.md, CHANGELOG.md

**Layer's Naming Conventions**

