�	�b+hZb@�b+hZb@!�b+hZb@	j:�GYV@j:�GYV@!j:�GYV@"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$�b+hZb@�=�$@M�?A��L��@Y�wJ�?*	�����%P@2F
Iterator::Model��t_�?!��i���F@)W�����?1�5N�:@:Preprocessing2j
3Iterator::Model::ParallelMap::Zip[1]::ForeverRepeatg��͒?!�ȶ�m<@)�zM
J�?1��,�#:@:Preprocessing2S
Iterator::Model::ParallelMapv�e��S�?!,�ϐ�%3@)v�e��S�?1,�ϐ�%3@:Preprocessing2d
-Iterator::Model::ParallelMap::Zip[0]::FlatMap��ԱJ�?!��~�3@)M�<i�?1��P���,@:Preprocessing2X
!Iterator::Model::ParallelMap::ZipnnLOX�?!%�4
K@)~�k�,	p?1׆ue�>@:Preprocessing2t
=Iterator::Model::ParallelMap::Zip[0]::FlatMap[0]::TensorSlice��Dׅl?!S���B@)��Dׅl?1S���B@:Preprocessing2v
?Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat::FromTensor��^(`;X?!��0�~Q@)��^(`;X?1��0�~Q@:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
device�Your program is NOT input-bound because only 2.9% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*moderate2A3.9 % of the total step time sampled is spent on All Others time.#You may skip the rest of this page.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	�=�$@M�?�=�$@M�?!�=�$@M�?      ��!       "      ��!       *      ��!       2	��L��@��L��@!��L��@:      ��!       B      ��!       J	�wJ�?�wJ�?!�wJ�?R      ��!       Z	�wJ�?�wJ�?!�wJ�?JCPU_ONLY2black"�
device�Your program is NOT input-bound because only 2.9% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"T
Rtensorflow_stats (identify the time-consuming operations executed on the CPU_ONLY)"Z
Xtrace_viewer (look at the activities on the timeline of each CPU_ONLY in the trace view)*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2�
=type.googleapis.com/tensorflow.profiler.GenericRecommendationQ
nomoderate"A3.9 % of the total step time sampled is spent on All Others time.:
Refer to the TF2 Profiler FAQ2"CPU: 