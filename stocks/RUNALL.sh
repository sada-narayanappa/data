# Run the following commands 
#
# set this in crontab by editing using the command "crontab -e"
# 
# CRON_TZ=MST
# */5 07-15 * * 1-5 /opt/data/data/stocks/RUNALL.sh
#
/opt/data/data/stocks/getstocks.py
/opt/data/data/stocks/01_prep_stocks.py
/opt/data/data/stocks/getnews.py

echo "Time: $(TZ=MST date). Ran." >> /tmp/crontab.log
