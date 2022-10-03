# SOOA_academic_record

## sooa_academic_record_db

sudo docker build -t sooa_academic_record_db .

sudo docker run -d -t -i -p 3307:3307 --name sooa_academic_record_db sooa_academic_record_db
    d397e5ae3b3f330ec76e381bcb7233735a5e89999ee3682f99494d1a590ffad7

sudo docker run --name db_sooa_client -d --link sooa_academic_record_db:db -p 8082:80 phpmyadmin
    e2993ab498a458aa9c48b4f175b4375465fa4ab20a63a686e8bd5325d24fe584

## sooa_academic_record_ms

sudo docker build -t sooa_academic_record_ms .

sudo docker run -p 4001:4001 -e DB_HOST=172.17.0.2 -e DB_PORT=3306 -e DB_USER=admin -e DB_PASSWORD=2022 -e DB_NAME=sooa_academic_record_db -e URL=0.0.0.0:4001 sooa_academic_record_ms
