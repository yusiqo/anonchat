#! /bin/sh

# clean shutdown of existing database

mariadb-admin shutdown

# kill any existing php server(s)

kill $(ps aux | grep '[p]hp' | awk '{print $2}')

# run php server as background task

# note: home directory is 'htdocs'

# run mysql as background task

# note: data directory assumed to be called 'data'

# You can put neccessary configs on command line, e.g.

mysqld_safe --datadir=$HOME/$REPL_SLUG/data  &

#--log-error=logfile.err --innodb-log-file-size=4194304 &

# Or build a custom my.cnf, set MYSQL_HOME and use that.

# Fiddly, but Unix environment variables aren't expanded in my.cnf so an effective way of being able to fork this repl without having to edit any config files.

cat <<EOT > $HOME/$REPL_SLUG/data/my.cnf

[server]

datadir=$HOME/$REPL_SLUG/data

#log-error=_database.err

#innodb-log-file-size=4194304

# I prefer case-insensitive table names

lower_case_table_names=1

#log-bin=binlog

EOT

export MYSQL_HOME=$HOME/$REPL_SLUG/data

echo $MYSQL_HOME

# Now start the mariadb server as a background task with the parameters in my.cnf

mysqld_safe &

# Logging is in nohup.out (shell log) & data/_database.log (database log)
