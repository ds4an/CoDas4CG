#!/bin/sh
set -e

for model in "model.wikisql.sup.exe_acc.lstm.hidden256.embed100.action100.field32.type32.dropout0.3.lr_decay0.5.pat5.beam5.vocab.bin.train.bin.col_att_affine.glorot.par_state_w_field_embed.seed0" "model.wikisql.sup.exe_acc.lstm.hidden256.embed100.action100.field32.type32.dropout0.3.lr_decay0.5.pat5.beam5.vocab.bin.train.bin.col_att_affine.glorot.par_state_w_field_embed.seed1" "model.wikisql.sup.exe_acc.lstm.hidden256.embed100.action100.field32.type32.dropout0.3.lr_decay0.5.pat5.beam5.vocab.bin.train.bin.col_att_affine.glorot.par_state_w_field_embed.seed2" "model.wikisql.sup.exe_acc.lstm.hidden256.embed100.action100.field32.type32.dropout0.3.lr_decay0.5.pat5.beam5.vocab.bin.train.bin.col_att_affine.glorot.no_par_info.seed0" "model.wikisql.sup.exe_acc.lstm.hidden256.embed100.action100.field32.type32.dropout0.3.lr_decay0.5.pat5.beam5.vocab.bin.train.bin.col_att_affine.glorot.no_par_info.seed1" "model.wikisql.sup.exe_acc.lstm.hidden256.embed100.action100.field32.type32.dropout0.3.lr_decay0.5.pat5.beam5.vocab.bin.train.bin.col_att_affine.glorot.no_par_info.seed2" 
do 
	source activate py3torch3cuda9
	CUDA_VISIBLE_DEVICES=${1:-0} python -u exp.py \
		--cuda \
     	--mode test \
     	--load_model saved_models/wikisql/${model}.bin \
     	--beam_size 5 \
     	--no_answer_prune \
     	--test_file data/wikisql/test.bin \
     	--save_decode_to decodes/wikisql/${model}.no_answer_prune.decode \
     	--decode_max_time_step 50  2>logs/wikisql/${model}.no_answer_prune.log
done
