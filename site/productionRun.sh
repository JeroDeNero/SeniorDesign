cd frontend/

ng build --prod
sudo npm install --global http-server
sudo ufw allow 8080/tcp
sudo ufw allow 3000/tcp
sudo ufw allow 5000/tcp
lite-server --baseDir="dist/site"
