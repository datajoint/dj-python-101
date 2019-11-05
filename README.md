(under active development - November 2019)

# License 
**Copyright, DataJoint Contributors, 2019**

The contents of this repository can be shared and adapted under the terms of the **Creative Commons Attribution-ShareAlike License Version 4.0** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

# DataJoint-Python 101

Welcome. These reference tutorial notebooks present all basic concepts for working with [DataJoint in Python](https://github.com/datajoint/datajoint-python)

DataJoint is a tool for managing shared computational workflows with scientific data.

This tutorial assumes intermediate programming proficiency in Python.

# Contents

### 0. Setup 
|Link|Topic|Link|Topic|
|:--|:--|:--|:--|
| **Connect** | install datajoint, configure database connection, `dj.config`, authentication, change password, save configuration, secure connection | **Admin** | configure database server, create user accounts, user privileges

### 1. Work with One Table
|Link|Topic|Link|Topic|
|:--|:--|:--|:--|
|[**Schema**](https://nbviewer.jupyter.org/github/datajoint/dj-python-101/blob/master/ch1/Schema.ipynb)| use `dj.schema` to create a new database schema or to connect to an existing one    | **Define** |  table class, simple attributes types, primary and secondary attributes, `describe` and `drop`.
|**Insert**| `insert`, `insert1`, `delete`, and `delete_quick`|**Fetch**| `fetch`, `fetch1`, `head`, `tail`, `len`.
|**Update**| when to use `update`
|**Restrict**| Query operators `&` and `-`. Restricted `delete`. |**Proj** | Query operator `proj`
|[**UUIDs**](https://nbviewer.jupyter.org/github/datajoint/dj-python-101/blob/master/ch1/UUID.ipynb)| work with `UUID` attributes | **Blobs** | storing complex data
|[**Attach**](https://nbviewer.jupyter.org/github/datajoint/dj-python-101/blob/master/ch1/Attach-Simple.ipynb) | storing entire files as attachments | **Lookup** | work with lookup tables |
|**Stores**| storing blobs and attachments in external stores | [**Filepath**](https://nbviewer.jupyter.org/github/datajoint/dj-python-101/blob/master/ch1/Filepaths.ipynb) | tracking files in an external repository |
|[**Adapters**](https://nbviewer.jupyter.org/github/datajoint/dj-python-101/blob/master/ch1/Adapted-Types.ipynb) | storing complex objects | [**Adapters-2**](https://nbviewer.jupyter.org/github/datajoint/dj-python-101/blob/master/ch1/Adapted-Types-2.ipynb) | storing complex objects with predefined schemas |
|[**Alter**](https://nbviewer.jupyter.org/github/datajoint/dj-python-101/blob/master/ch1/Alter.ipynb) | Altering table definitions with `alter`
|[**Indexes**](https://nbviewer.jupyter.org/github/datajoint/dj-python-101/blob/master/ch1/Indexes.ipynb)| speed up queries | **Transactions** | defining atomic transactions
|**Log**| using `schema.log`

### 2. Work with Multiple Tables
|Link|Topic|Link|Topic|
|:--|:--|:--|:--|
|**Modules**|  correspondence between schemas and modules | **Dependencies** |  primary and secondary dependencies, referential constraints, cascading deletes 
|**Existing**| find and connect to existing schemas: `dj.list_schemas`, `schema.spawn_missing_classes`, `dj.create_virtual_modules` | **Diagrams** | `dj.Diagram`, graph algebra, multi-schema databases |
|**Join**| query operator `*`, restricting `&` with a query, using `proj` to control join | **Aggregate**| query operator `.aggr`
|**U**| Using universal sets `dj.U` in restrictions, aggregations, and joins. | **Union** query operator `+`.
|**DerivedDependencies**| using the `proj` operator in dependencies | **UniqueDependencies** | unique and nullable dependencies

### 3. Data modeling
|Link|Topic|Link|Topic|
|:--|:--|:--|:--|
| **Hierarchy** | modeling hierarchical or nested data | **Dimensional** |  modeling dimensional relationships
| **Master-Part** | modeling master-part relationships | **Specialization** | modeling specialization relationships |
| **Association** | modeling associations between entities, including groups | **Cyclic** | modeling cyclic relationships | 

### 4. Computation
|Link|Topic|Link|Topic|
|:--|:--|:--|:--|
| **Populate** | the `populate` method and the `make` callback in `dj.Imported` and `dj.Computed` tables | **Distributed** | using `populate` with `reserve_jobs=True` 
| **Jobs** | working with `schema.jobs` and `dj.kill` | **Compute-Parts** | computations in a master-part relationship
| **Params** | computation parameters and computation versioning | **KeySource** | controlling the scope and granularity of computing jobs with `key_source`
| **GitHash** | marking computations with a git tag
| **Offline** | work with no database connection

### 5. Data Sharing and Migration
|Link|Topic|Link|Topic|
|:--|:--|:--|:--|
| **Export** | exporting data for dataset sharing

### 6. Interfaces & Applications
|Link|Topic|Link|Topic|
|:--|:--|:--|:--|
| **WebGUI** | web interfaces | **Slack** | Slack integration 

### 7. Questions and Examples
|Link|Topic|Link|Topic|
|:--|:--|:--|:--|
|[**NWB-Adapter**](https://nbviewer.jupyter.org/github/datajoint/dj-python-101/blob/master/ch7/NWB-Adapter.ipynb) | Work with NWB Files
