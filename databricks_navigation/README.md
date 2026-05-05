# Databricks navigation

- theory
- UI navigation


## Databricks Overview
Databricks is a unified data platform for building enterprise-level cloud infrastrucutre, including components like data lakehouse, data pipeline, BI, data science/AI and data governance. It provides a collaborative workspace for data engineers, data analysts, data scientists, ML engineers, data owners and other data roles to develop and share in the same platform. 


<img src="https://github.com/kokchun/assets/blob/main/databricks/databricks_overview.png?raw=true" alt="intro to cloud computing" width="600">


### Data Lakehouse
A data lakehouse merges the best of data lakes and data warehouses. While it allows enterprises to store raw data in its native format (like a data lake), it also enables the creation of delta tables, bringing warehouse-like advantages such as ACID transactions, schema enforcement, and fine-grained access control. 

### Data pipeline
Enterprises can run their data pipelines using databricks's computing resources. The ELT logic and orchestration can be defined using Spark and SQL with Lakeflow Spark Declarative Pipeline and Lakeflow Job. 

### Business Intelligence
Dashboards can be created and shared to other users on databricks, allowing visualization to be hosted on the same platform as the data inputs to the visualization. 

### Data Science & AI
Data scientists and machine learning engineer can train, deploy and serve their classical ML and AI models using the computer resources in databricks. They are also able to manage the entire ML lifecycle with MLflow. 

### Data Governance
Enterprises can use Unity Catalog as a single tool to manage premissions for both data objects and models. 

## Databricks UI 
Once you have signed up for the free edition of databricks, you can create and manage all resources in databricks through the web UI. Let's navigate through the UI to overview the major databricks resources:

### Workspace
A workspace is a Databricks deployment in the cloud that acts as an environment to keep all of your Databricks resources. 

You can switch between different workspace environments by selecting a workspace on the upper right hand corner:


<img src="https://github.com/kokchun/assets/blob/main/databricks/choose_workspace.png?raw=true" alt="intro to cloud computing" width="600">


The workspace browser icon on the left sidebar will lead you to your workspace file system where you can store your files like scripts: 


<img src="https://github.com/kokchun/assets/blob/main/databricks/workspace_browser.png?raw=true" alt="intro to cloud computing" width="600">


### Catalog
Catalog is the place to organize your data assets in Databricks. You can create multiple catalogs and each catalog should represent a logical category of data. You can further isolate your data assets into schemas under a catalog, which are categories that are more granular than catalogs. Under a schema, you can store non-tabular data assets under Volumes and tables under Tables:


<img src="https://github.com/kokchun/assets/blob/main/databricks/catalog.png?raw=true" alt="intro to cloud computing" width="600">


### Notebook
You can create a notebook to keep and run your scripts in Python and sql. You can organize your notebook location in your workspace file system. For Python scripts, you can manage your dependencies by opening the Python environment pane on the right panel:


<img src="https://github.com/kokchun/assets/blob/main/databricks/notebook.png?raw=true" alt="intro to cloud computing" width="600">


### Compute 
You need computing resources to run your scripts on the cloud. Enterprises users can create different types of computing resources that are optimal for their use cases. However, for free edition, you will be using a default serverless computing resources configured by Databricks:


<img src="https://github.com/kokchun/assets/blob/main/databricks/compute.png?raw=true" alt="intro to cloud computing" width="600">


### Sql editor
You can use the SQL Editor in the UI to quickly run sql queries against your data assets in your catalogs. You can choose to show your results as tabel or visualization:


<img src="https://github.com/kokchun/assets/blob/main/databricks/sql.png?raw=true" alt="intro to cloud computing" width="600">


### Jobs & pipelines


### Dashboard 


## Read More 👓
[What is Databricks?](https://docs.databricks.com/aws/en/introduction/)

[Databricks components](https://docs.databricks.com/aws/en/getting-started/concepts)
