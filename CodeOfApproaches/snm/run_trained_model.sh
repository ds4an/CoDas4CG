output="runs"
device="cpu"

if [ "$1" == "hs" ]; then
	# hs dataset
	echo "run trained model for hs"
	dataset="data/hs.freq1.max_action350.pre_suf.unary_closure.bin"
	model="/home1/zjq/try3/NL2code-master2/runs/model.iter900.npz"
	commandline="-decode_max_time_step 500 -rule_embed_dim 256 -node_embed_dim 256"
	datatype="django"
else
	# django dataset
	echo "run trained model for django"
	dataset="data/django.cleaned.dataset.freq5.par_info.refact.space_only.bin"
	model="model.django_word128_encoder256_rule128_node64.beam15.adam.simple_trans.no_unary_closure.8e39832.run3.best_acc.npz"
	commandline="-rule_embed_dim 128 -node_embed_dim 64"
	datatype="django"
fi

# decode the test set and save the nbest decoding results
THEANO_FLAGS="mode=FAST_RUN,device=${device},floatX=float32" python code_gen.py \
-data_type ${datatype} \
-data ${dataset} \
-output_dir ${output} \
-model models/${model} \
${commandline} \
decode \
-saveto ${output}/${model}.decode_results.test.bin

# evaluate the decoding result
python code_gen.py \
	-data_type ${datatype} \
	-data ${dataset} \
	-output_dir ${output} \
	evaluate \
	-input ${output}/${model}.decode_results.test.bin | tee ${output}/${model}.decode_results.test.log
