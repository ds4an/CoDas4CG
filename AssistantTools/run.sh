 #!/bin/bash
 for j in `find . -name "*.py"`
 do
# $(basename $j .py)
x=`expr $(basename $j .py)`
#echo $x
python $j < "./pre/"${x}.in
#echo -e >> a.out
 done
