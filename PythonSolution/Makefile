STREAMING = /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar

USER=$(shell whoami)

export HADOOP_CLASSPATH=/usr/lib/jvm/java-8-openjdk-amd64/lib/tools.jar

filesystem:
	-hdfs dfs -mkdir /user
	-hdfs dfs -mkdir /user/$(USER)

prepare:
	-hdfs dfs -rm -r input
	-hdfs dfs -mkdir input
	hdfs dfs -put ~/cite75_99.txt input/cite75_99.txt
	hdfs dfs -put ~/apat63_99.txt input/apat63_99.txt

stream:
	sh ./RUN-MAP-REDUCE-1
