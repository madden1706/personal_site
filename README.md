## www.madresearchden.com

This is my personal site.

---

The project consists of Docker containers for:
- a Django app
- a postgres database
- certbot ssl certificate creation
- a bokeh server for interative plots
- an nginx web server

---

The script init-letsencrypt.sh is used to get a dummy ssl cert, start nginx and the request real ssl certs via certbot. 


### Containers

```shell
docker push docker.pkg.github.com/madden1706/madresearchden/website:0.1.1 
```

```shell
```

#### website

#### bokeh Vesions

#### nginx

#### posgres

To create an ssh tunnel to the remote machine where the database is:

```shell
ssh mrd_linode -L 5432:127.0.0.1:5432 -N
```
