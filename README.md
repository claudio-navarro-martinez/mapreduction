mapreduction
============

another example for map reduction in python

hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.5.2.jar \
-D mapreduce.job.reduces=1 \
-input /user/claudio/NASA_access_log_Aug95 \
-output /user/claudio/output/kk4.output \
-file /home/hadoop/map2.py 
-file /home/hadoop/red2.py \
-mapper /home/hadoop/map2.py  \
-reducer /home/hadoop/red2.py
