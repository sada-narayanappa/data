# bash script /opt/data/tseries/models/default__a1.csv__Link_Model/analz_a2.csv.cfg.csv.sh
# --
cd /opt/data/tseries/models/default__a1.csv__Link_Model/
OPTS=""

/opt/utils/SCORE.EXE -i model.txt -t a2.csv.cfg.csv -o score__a2.csv.cfg.csv.txt -A 500
python -m tseriesutils.combine_scores

echo "#FINISHED @" `date` >> analz_a2.csv.cfg.csv.sh
#FINISHED @ Fri Sep 15 01:43:21 UTC 2023
