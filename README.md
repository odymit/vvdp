# Vehicle Vulnerability Display Platform
vvdp is a simple vulnerability display platform, and the techs we used are list below to build it:
- Frontend: vue
- Backend: Django
- Search: meilisearch

The `vue-admin-template` can be found [here](https://github.com/PanJiaChen/vue-admin-template).
## requirements
```
Python 3.10.4

Package             Version
------------------- ---------
asgiref             3.4.1
certifi             2021.10.8
charset-normalizer  2.0.12
Django              4.0.1
django-cors-headers 3.11.0
idna                3.3
meilisearch         0.18.0
pip                 22.1
PyMySQL             1.0.2
requests            2.27.1
setuptools          58.1.0
sqlparse            0.4.2
urllib3             1.26.8


npm@8.4.1 
node/v16.7.0

```
## how to use
```
source venv/bin/activate
cd vvdp
python manage.py runserver 8080

cd ../vue-admin-template
npm run serve

# install meilisearch
docker pull getmeili/meilisearch:latest
docker run -it --rm \\n    -p 7700:7700 \\n    -v $(pwd)/data.ms:/data.ms \\n    getmeili/meilisearch:latest
# import data
cd ../meilisearch
python upload_json.py


```
