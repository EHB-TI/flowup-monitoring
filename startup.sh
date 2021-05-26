sudo sysctl -w vm.max_map_count=262144
sudo apt-get update
sudo apt-get install python3-pip
pip3 install -r ./requirements.txt
docker-compose down -v
file=".env"
if [ -f "$file" ] ; then
    rm "$file"
fi
cp .env.example .env
cd init
python3 initialise.py 
cd ..
sed -i '$d' .env
sed -i '$d' .env
value=$(<./init/login.txt)
echo "$value" | tee -a .env
docker-compose down
docker-compose up -d
rm ./init/login.txt
rm ./init/temp.txt