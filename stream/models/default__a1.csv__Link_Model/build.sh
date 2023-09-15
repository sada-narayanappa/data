# bash script /opt/data/tseries/models/default__a1.csv__Link_Model/build.sh
# --
cd /opt/data/tseries/models/default__a1.csv__Link_Model/
rm -f FINISHED
MIN_SCORE=0.5
FILTER="-e 0.7 -b 0.5" 

#--
/opt/utils/INVX.EXE -t /opt/data/tseries/models/default__a1.csv__Link_Model/train.csv -m $MIN_SCORE -o /opt/data/tseries/models/default__a1.csv__Link_Model/model.txt.1
/opt/utils/inv_filter.py  $FILTER -o /opt/data/tseries/models/default__a1.csv__Link_Model/model.txt /opt/data/tseries/models/default__a1.csv__Link_Model/model.txt.1
/opt/utils/SCORE.EXE -i /opt/data/tseries/models/default__a1.csv__Link_Model/model.txt -t /opt/data/tseries/models/default__a1.csv__Link_Model/train.csv -o score__train.csv.txt -A 500
cp score__train.csv.txt SCORES.txt
#--
echo "#FINISHED /opt/data/tseries/models/default__a1.csv__Link_Model/build.sh : " `date` > /opt/data/tseries/models/default__a1.csv__Link_Model/FINISHED
