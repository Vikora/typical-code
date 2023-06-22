# Spark VS MapReduce

Spark and MapReduce are both __distributed data processing frameworks__ used for big data analytics. Spark offers improved performance, easier development, real-time processing capabilities, and a more extensive ecosystem compared to MapReduce. However, MapReduce still has its place in scenarios where batch processing with Hadoop integration is the primary requirement.

## Differences in terms of performance, ease of use, and functionality

* Processing Model

  * **MapReduce** follows a two-step processing model where data is processed in two stages - map and reduce. The map function takes input data and transforms it into intermediate key-value pairs, and then the reduce function aggregates and summarizes these pairs to produce the final output.
  * **Spark** introduces the concept of Resilient Distributed Datasets (RDDs), which are distributed collections of objects. Spark performs in-memory computations, allowing data to be cached in memory across multiple iterations, resulting in faster processing.

* Performance
 
  * **MapReduce** processes data by __writing intermediate results to disk after each stage__, which can cause significant I/O overhead. As a result, it is better suited for batch processing workloads with large datasets but suffers from slower execution times for iterative algorithms or interactive data analysis.
  * **Spark** keeps __data in memory as RDDs__, which enables faster data processing as it avoids excessive disk I/O. Additionally, Spark's ability to __cache intermediate data in memory__ makes it more efficient __for iterative computations and interactive queries__, resulting in improved performance compared to MapReduce.

* Ease of Use

  * **MapReduce** requires developers to write more low-level code to define map and reduce functions explicitly. Developers need to handle many details such as data serialization, partitioning, and distributed synchronization, making it more complex and time-consuming.
  * **Spark** provides a high-level API that simplifies the development process. It offers libraries for various languages (e.g., Scala, Java, Python) and supports a rich set of operators and transformations, making it easier to express complex computations. Spark also integrates well with other big data tools like Hadoop, Hive, and HBase.

* Real-time Processing

  * **MapReduce** is primarily designed __for batch processing__, and although it can be used for near-real-time processing, it is not well-suited for low-latency data processing.
  * **Spark's** in-memory computing capabilities make it __suitable for real-time and stream processing__ use cases. It provides a streaming API called Structured Streaming, which allows developers to process data in real-time and integrate batch and streaming processing seamlessly.

* Ecosystem

  * **MapReduce** is part of the Apache Hadoop ecosystem and works well with other Hadoop components like HDFS (Hadoop Distributed File System), Hive, and Pig.
  * **Spark** has a broader ecosystem and supports various data sources, including HDFS, Apache Cassandra, Apache Kafka, and many more. It also provides libraries for machine learning (Spark MLlib), graph processing (GraphX), and SQL-based analytics (Spark SQL).


# Glossary

* **RDD (Resilient Distributed Dataset)** is a low-level data structure in Apache Spark. RDDs are an immutable distributed collection of objects that can be processed in parallel across a cluster of machines.
  * RDDs are resilient because they can reconstruct lost partitions. This resilience is achieved through lineage information, which tracks the series of transformations applied to the base dataset. By using lineage, Spark can recompute lost or damaged partitions by replaying the transformations from the source data.
  * RDD serialize and de-serialize data when it distributes across a cluster (repartition & shuffling).
* **DataFrame** is a distributed collection of structured data organized into named columns, similar to a table in a relational database.
  * Off-heap storage for data in binary format.
  * Encoder code on the fly to work with this binary format for your specific objects. 
* **Dataset**
* **SparkSession** - an entry point to underlying Spark functionality in order to programmatically create Spark RDD, DataFrame, and DataSet.


# Catalyst Optimizer
is a query optimization framework in Apache Spark. It is responsible for optimizing and transforming the logical and physical execution plans of Spark SQL queries, DataFrame, and Dataset operations. The goal of the Catalyst Optimizer is to generate an efficient execution plan that can be executed on distributed clusters.

![Catalyst-Optimizer-diagram](https://www.databricks.com/wp-content/uploads/2018/05/Catalyst-Optimizer-diagram.png)

# Cache and persist
