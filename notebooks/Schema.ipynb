{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Schema\n",
    "\n",
    "A **schema** is a namespace for a collection of related tables in the database. The words \"schema\" and \"database\" can be used interchangeably in DataJoint, but \"schema\" is preferred. A single data pipeline can include multiple schemas. This notebook covers creating new schemas or connecting to existing ones. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'0.12.dev7'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import datajoint as dj\n",
    "dj.__version__"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The function call `dj.schema(schema_name)` make an object that references the named schema. If this is a new schema, then `dj.schema` will create it on the server.\n",
    "\n",
    "It is a common convention to name the returned object `schema` and we will follow this convention throughout this course. This implies that separate Python modules are created to work with each schema on the database server. We will follow this convention also: 1 Python module $\\equiv$ 1 database schema.\n",
    "\n",
    "You need `schema` to create new tables within this schema."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Connecting dimitri@localhost:3306\n"
     ]
    }
   ],
   "source": [
    "# create the dj101_university database\n",
    "schema = dj.schema('dj101_university')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The `schema` object is used as the **decorator** for DataJoint table classes. \n",
    "\n",
    "For example, let's create a table to represent university departments."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "@schema\n",
    "class Department(dj.Manual):\n",
    "    definition = \"\"\"\n",
    "    department : char(8)  # short name\n",
    "    ---\n",
    "    department_name : varchar(255)  # department name\n",
    "    \"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The new table is declared on the database server when the decorator executes, so the table becomes ready for use:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "Department.insert1((\"MATH\", \"Department of Mathematics\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        \n",
       "        <style type=\"text/css\">\n",
       "            .Relation{\n",
       "                border-collapse:collapse;\n",
       "            }\n",
       "            .Relation th{\n",
       "                background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid;\n",
       "                font-weight: normal; font-family: monospace; font-size: 100%;\n",
       "            }\n",
       "            .Relation td{\n",
       "                padding:4px; border:#f0e0e0 1px solid; font-size:100%;\n",
       "            }\n",
       "            .Relation tr:nth-child(odd){\n",
       "                background: #ffffff;\n",
       "            }\n",
       "            .Relation tr:nth-child(even){\n",
       "                background: #f3f1ff;\n",
       "            }\n",
       "            /* Tooltip container */\n",
       "            .djtooltip {\n",
       "            }\n",
       "            /* Tooltip text */\n",
       "            .djtooltip .djtooltiptext {\n",
       "                visibility: hidden;\n",
       "                width: 120px;\n",
       "                background-color: black;\n",
       "                color: #fff;\n",
       "                text-align: center;\n",
       "                padding: 5px 0;\n",
       "                border-radius: 6px;\n",
       "                /* Position the tooltip text - see examples below! */\n",
       "                position: absolute;\n",
       "                z-index: 1;\n",
       "            }\n",
       "            #primary {\n",
       "                font-weight: bold;\n",
       "                color: black;\n",
       "            }\n",
       "\n",
       "            #nonprimary {\n",
       "                font-weight: normal;\n",
       "                color: white;\n",
       "            }\n",
       "\n",
       "            /* Show the tooltip text when you mouse over the tooltip container */\n",
       "            .djtooltip:hover .djtooltiptext {\n",
       "                visibility: visible;\n",
       "            }\n",
       "        </style>\n",
       "        \n",
       "        <b></b>\n",
       "            <div style=\"max-height:1000px;max-width:1500px;overflow:auto;\">\n",
       "            <table border=\"1\" class=\"Relation\">\n",
       "                <thead> <tr style=\"text-align: right;\"> <th> <div class=\"djtooltip\">\n",
       "                                <p id=\"primary\">department</p>\n",
       "                                <span class=\"djtooltiptext\">short name</span>\n",
       "                            </div></th><th><div class=\"djtooltip\">\n",
       "                                <p id=\"nonprimary\">department_name</p>\n",
       "                                <span class=\"djtooltiptext\">department name</span>\n",
       "                            </div> </th> </tr> </thead>\n",
       "                <tbody> <tr> <td>MATH</td>\n",
       "<td>Department of Mathematics</td> </tr> </tbody>\n",
       "            </table>\n",
       "            \n",
       "            <p>Total: 1</p></div>\n",
       "            "
      ],
      "text/plain": [
       "*department    department_nam\n",
       "+------------+ +------------+\n",
       "MATH           Department of \n",
       " (Total: 1)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Department()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can view all accessible schemas on the database server:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['dimitri_alter',\n",
       " 'dimitri_attach',\n",
       " 'dimitri_blob',\n",
       " 'dimitri_blobs',\n",
       " 'dimitri_debug',\n",
       " 'dimitri_filepath',\n",
       " 'dimitri_nphoton',\n",
       " 'dimitri_nwb',\n",
       " 'dimitri_schema',\n",
       " 'dimitri_singular',\n",
       " 'dimitri_social',\n",
       " 'dimitri_test',\n",
       " 'dimitri_tutorial',\n",
       " 'dimitri_unique',\n",
       " 'dimitri_university',\n",
       " 'dimitri_uuid',\n",
       " 'dj101_university',\n",
       " 'test_attach',\n",
       " 'test_external',\n",
       " 'test_filepath',\n",
       " 'test_graphs',\n",
       " 'test_graphs_external',\n",
       " 'test_graps',\n",
       " 'test_mikkel',\n",
       " 'test_orders',\n",
       " 'test_parse',\n",
       " 'test_question001',\n",
       " 'test_question002',\n",
       " 'test_unique',\n",
       " 'university']"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dj.list_schemas()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Keyword arguments `create_schema` and `create_tables`\n",
    "If you wish to connect to existing schema, you might like to set `create_schema=False` to prevent accidental creation of a new schema from a misspelled schema name:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'datajoint.errors.DataJointError'> Database named `dj101_misspelled` was not defined. Set argument create_schema=True to create it.\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    schema = dj.schema('dj101_misspelled', create_schema=False)\n",
    "except dj.DataJointError as err:\n",
    "    print(type(err), err)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Also, if you connect to existing schema without the intention of extending it with new tables, set `create_tables=False`. This is a good practice for modules that are deployed for routine use after the active design phase. This obsolete copies of the module will not attempt to re-create deprecated tables:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "schema = dj.schema('dj101_university', create_schema=False, create_tables=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'datajoint.errors.DataJointError'> Table `deprecated` not declared\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    @schema\n",
    "    class Deprecated(dj.Manual):\n",
    "        definition = \"\"\"\n",
    "        a : int    \n",
    "        \"\"\"\n",
    "except dj.DataJointError as err:\n",
    "    print(type(err), err)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Other arguments of `dj.schema`\n",
    "\n",
    "`dj.schema` also takes a `context` argument. It largely unnecessary now. In early versions of DataJoint for python, this argument was used to pass into it the name space in which to look for table class declarations. In some old DataJoint code, you may still find something like `schema = dj.schema('pipeline_ephys', locals())`. Unless you wish to explicitly set the contenxt in which the schema object should find class names, omit this value.\n",
    "\n",
    "The `connection` argument is provided for the rare cases when it is necessary to explicitly define the database connection instead of using the default connection that is accessible by calling `dj.conn()`. This may be helpful when multiple database connections are accessed simultaneously.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Dropping a schema\n",
    "Dropping the schema should be done with extreme caution. It's the quickest way to lose lots of data very quickly. `schema.drop` removes the table contents and table defintions for the entire schema."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Proceed to delete entire schema `dj101_university`? [yes, No]: yes\n"
     ]
    }
   ],
   "source": [
    "schema.drop()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Troubleshooting\n",
    "\n",
    "The most common problems related to the use of `dj.schema` are user privileges. If you do not have priviliges to create a schema with a specific name or specific name pattern, a `dj.errors.AccessError` will occur:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'datajoint.errors.AccessError'> ('Insufficient privileges.', \"Access denied for user 'dimitri'@'%' to database 'some_schema'\", 'CREATE DATABASE `some_schema`')\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    schema = dj.schema('some_schema')\n",
    "except dj.DataJointError as err:\n",
    "    print(type(err), err)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
