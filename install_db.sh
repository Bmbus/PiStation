# install apeche2 webserver
sudo apt install apache2 -y

cd /var/www/html

ls -al

hostname -i

# install mariadb
sudo apt install mariadb-server php-mysql -y

sudo service apache2 restart

sudo mysql_secure_installation

# install phpmyadmin
sudo apt install phpmyadmin -y

sudo phpenmod mysqli

sudo service apache2 restart

sudo ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin

# get ip address and go to website + print ip!!